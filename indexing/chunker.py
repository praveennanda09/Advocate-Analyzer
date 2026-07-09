from typing import List, Dict, Any
from validator.schema_validator import CaseRecordSchema

class Chunker:
    """Transforms structured case data into textual documents for embedding indexation."""
    
    @staticmethod
    def create_case_chunks(case: CaseRecordSchema) -> List[Dict[str, Any]]:
        """Create semantic text chunks from a case record, maintaining metadata context."""
        chunks = []
        cnr = case.cnr
        case_num = case.case_number
        
        # 1. Main case summary paragraph
        summary_text = (
            f"Case Summary:\n"
            f"CNR Number: {cnr}\n"
            f"Case Number: {case_num}\n"
            f"Court: {case.court}\n"
            f"Presiding Judge: {case.judge or 'Not specified'}\n"
            f"Case Category: {case.case_category or 'Not specified'}\n"
            f"Filing Date: {case.filing_date or 'Not specified'}\n"
            f"Status: {case.status}\n"
            f"Current Stage: {case.current_stage or 'Not specified'}\n"
            f"Petitioner: {case.petitioner} (Advocate: {case.petitioner_advocate or 'Not specified'})\n"
            f"Respondent: {case.respondent} (Advocate: {case.respondent_advocate or 'Not specified'})\n"
        )
        if case.disposal_date:
            summary_text += f"Disposal Date: {case.disposal_date}\n"
            
        chunks.append({
            "text": summary_text,
            "metadata": {
                "cnr": cnr,
                "case_number": case_num,
                "type": "summary",
                "court": case.court,
                "petitioner_advocate": case.petitioner_advocate,
                "respondent_advocate": case.respondent_advocate
            }
        })
        
        # 2. Acts and Sections chunks
        if case.acts:
            acts_text = f"Governing Acts and Sections for Case {case_num} (CNR: {cnr}):\n"
            for index, act in enumerate(case.acts, 1):
                acts_text += f"{index}. Act: {act.act}, Section: {act.section}\n"
                
            chunks.append({
                "text": acts_text,
                "metadata": {
                    "cnr": cnr,
                    "case_number": case_num,
                    "type": "acts"
                }
            })
            
        # 3. Hearing history chunks
        if case.hearing_history:
            hearings_text = f"Hearing History and Timeline for Case {case_num} (CNR: {cnr}):\n"
            for h in case.hearing_history:
                hearings_text += f"- Date: {h.hearing_date or 'N/A'}, Stage: {h.stage}, Action/Business: {h.business}\n"
                
            chunks.append({
                "text": hearings_text,
                "metadata": {
                    "cnr": cnr,
                    "case_number": case_num,
                    "type": "hearings"
                }
            })

        # 4. Orders chunks
        if case.orders:
            orders_text = f"Court Orders and Judgments issued for Case {case_num} (CNR: {cnr}):\n"
            for o in case.orders:
                orders_text += f"- Date: {o.date or 'N/A'}, Description: {o.description}, PDF Document: {o.pdf_url}\n"
                
            chunks.append({
                "text": orders_text,
                "metadata": {
                    "cnr": cnr,
                    "case_number": case_num,
                    "type": "orders"
                }
            })
            
        return chunks

    @classmethod
    def chunk_all_cases(cls, cases: List[CaseRecordSchema]) -> List[Dict[str, Any]]:
        """Process multiple cases and extract all textual chunks."""
        all_chunks = []
        for case in cases:
            all_chunks.extend(cls.create_case_chunks(case))
        return all_chunks
