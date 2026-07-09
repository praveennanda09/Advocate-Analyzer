import os
import json
import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional
import pandas as pd
from validator.schema_validator import CaseRecordSchema, ActSchema, HearingSchema, OrderSchema

class BaseRepository:
    """Base interface for case history storage backends."""
    def save_case(self, case: CaseRecordSchema):
        raise NotImplementedError()
        
    def get_case(self, cnr: str) -> Optional[CaseRecordSchema]:
        raise NotImplementedError()
        
    def list_cases(self) -> List[CaseRecordSchema]:
        raise NotImplementedError()

class SQLiteRepository(BaseRepository):
    """SQLite implementation of the repository storage."""
    
    def __init__(self, db_path: str):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            # Main cases table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS cases (
                    cnr TEXT PRIMARY KEY,
                    case_number TEXT,
                    filing_date TEXT,
                    registration_date TEXT,
                    disposal_date TEXT,
                    current_stage TEXT,
                    status TEXT,
                    court TEXT,
                    judge TEXT,
                    case_category TEXT,
                    petitioner TEXT,
                    petitioner_advocate TEXT,
                    respondent TEXT,
                    respondent_advocate TEXT,
                    metadata TEXT
                )
            """)
            # Associated tables
            conn.execute("""
                CREATE TABLE IF NOT EXISTS acts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cnr TEXT,
                    act TEXT,
                    section TEXT,
                    FOREIGN KEY(cnr) REFERENCES cases(cnr) ON DELETE CASCADE
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS hearing_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cnr TEXT,
                    hearing_date TEXT,
                    stage TEXT,
                    business TEXT,
                    FOREIGN KEY(cnr) REFERENCES cases(cnr) ON DELETE CASCADE
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cnr TEXT,
                    date TEXT,
                    description TEXT,
                    pdf_url TEXT,
                    FOREIGN KEY(cnr) REFERENCES cases(cnr) ON DELETE CASCADE
                )
            """)
            conn.commit()

    def save_case(self, case: CaseRecordSchema):
        with sqlite3.connect(self.db_path) as conn:
            # Insert or replace case
            conn.execute("""
                INSERT OR REPLACE INTO cases (
                    cnr, case_number, filing_date, registration_date, disposal_date,
                    current_stage, status, court, judge, case_category,
                    petitioner, petitioner_advocate, respondent, respondent_advocate,
                    metadata
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                case.cnr, case.case_number, case.filing_date, case.registration_date, case.disposal_date,
                case.current_stage, case.status, case.court, case.judge, case.case_category,
                case.petitioner, case.petitioner_advocate, case.respondent, case.respondent_advocate,
                json.dumps(case.metadata)
            ))
            
            # Clear old acts, history, and orders for this case to avoid duplicates
            conn.execute("DELETE FROM acts WHERE cnr = ?", (case.cnr,))
            conn.execute("DELETE FROM hearing_history WHERE cnr = ?", (case.cnr,))
            conn.execute("DELETE FROM orders WHERE cnr = ?", (case.cnr,))
            
            # Insert acts
            for act in case.acts:
                conn.execute(
                    "INSERT INTO acts (cnr, act, section) VALUES (?, ?, ?)",
                    (case.cnr, act.act, act.section)
                )
                
            # Insert hearings
            for hearing in case.hearing_history:
                conn.execute(
                    "INSERT INTO hearing_history (cnr, hearing_date, stage, business) VALUES (?, ?, ?, ?)",
                    (case.cnr, hearing.hearing_date, hearing.stage, hearing.business)
                )
                
            # Insert orders
            for order in case.orders:
                conn.execute(
                    "INSERT INTO orders (cnr, date, description, pdf_url) VALUES (?, ?, ?, ?)",
                    (case.cnr, order.date, order.description, order.pdf_url)
                )
                
            conn.commit()

    def get_case(self, cnr: str) -> Optional[CaseRecordSchema]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            # Get main record
            cursor.execute("SELECT * FROM cases WHERE cnr = ?", (cnr,))
            row = cursor.fetchone()
            if not row:
                return None
                
            # Get acts
            cursor.execute("SELECT act, section FROM acts WHERE cnr = ?", (cnr,))
            acts = [ActSchema(act=r["act"], section=r["section"]) for r in cursor.fetchall()]
            
            # Get hearings
            cursor.execute("SELECT hearing_date, stage, business FROM hearing_history WHERE cnr = ?", (cnr,))
            hearings = [HearingSchema(hearing_date=r["hearing_date"], stage=r["stage"], business=r["business"]) for r in cursor.fetchall()]
            
            # Get orders
            cursor.execute("SELECT date, description, pdf_url FROM orders WHERE cnr = ?", (cnr,))
            orders = [OrderSchema(date=r["date"], description=r["description"], pdf_url=r["pdf_url"]) for r in cursor.fetchall()]
            
            meta = json.loads(row["metadata"]) if row["metadata"] else {}
            
            return CaseRecordSchema(
                cnr=row["cnr"],
                case_number=row["case_number"],
                filing_date=row["filing_date"],
                registration_date=row["registration_date"],
                disposal_date=row["disposal_date"],
                current_stage=row["current_stage"],
                status=row["status"],
                court=row["court"],
                judge=row["judge"],
                case_category=row["case_category"],
                petitioner=row["petitioner"],
                petitioner_advocate=row["petitioner_advocate"],
                respondent=row["respondent"],
                respondent_advocate=row["respondent_advocate"],
                acts=acts,
                hearing_history=hearings,
                orders=orders,
                metadata=meta
            )

    def list_cases(self) -> List[CaseRecordSchema]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT cnr FROM cases")
            cnrs = [row[0] for row in cursor.fetchall()]
            
        cases = []
        for cnr in cnrs:
            case = self.get_case(cnr)
            if case:
                cases.append(case)
        return cases


class JSONLRepository:
    """Appends raw case information as JSON lines to a flat backup file."""
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        
    def save_case(self, case: CaseRecordSchema):
        data = case.model_dump()
        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(data) + "\n")
            
    def list_cases(self) -> List[CaseRecordSchema]:
        if not self.file_path.exists():
            return []
            
        cases = []
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    data = json.loads(line)
                    cases.append(CaseRecordSchema(**data))
        return cases


class ParquetRepository:
    """Saves flat case representations into Apache Parquet columnar files for data analysis."""
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        
    def save_all(self, cases: List[CaseRecordSchema]):
        """Convert a list of CaseRecordSchemas to a flat dataframe and save to Parquet."""
        flat_records = []
        for case in cases:
            flat_records.append({
                "cnr": case.cnr,
                "case_number": case.case_number,
                "filing_date": case.filing_date,
                "registration_date": case.registration_date,
                "disposal_date": case.disposal_date,
                "current_stage": case.current_stage,
                "status": case.status,
                "court": case.court,
                "judge": case.judge,
                "case_category": case.case_category,
                "petitioner": case.petitioner,
                "petitioner_advocate": case.petitioner_advocate,
                "respondent": case.respondent,
                "respondent_advocate": case.respondent_advocate,
                "num_acts": len(case.acts),
                "num_hearings": len(case.hearing_history),
                "num_orders": len(case.orders)
            })
            
        df = pd.DataFrame(flat_records)
        df.to_parquet(self.file_path, index=False)

    def load_dataframe(self) -> pd.DataFrame:
        """Load the Parquet file back into a Pandas dataframe."""
        if not self.file_path.exists():
            return pd.DataFrame()
        return pd.read_parquet(self.file_path)
