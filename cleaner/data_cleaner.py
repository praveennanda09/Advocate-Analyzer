import re
from datetime import datetime
from typing import Optional, List, Dict, Any

class DataCleaner:
    """Provides methods for cleaning and normalizing scraped legal data fields."""
    
    @staticmethod
    def clean_whitespace(text: Optional[str]) -> str:
        """Strip HTML spaces, normalize extra whitespace, newlines, and tabs."""
        if not text:
            return ""
        # Replace multiple spaces/newlines/tabs with a single space
        cleaned = re.sub(r'\s+', ' ', text)
        return cleaned.strip()

    @staticmethod
    def parse_date(date_str: Optional[str]) -> Optional[str]:
        """Convert dynamic eCourts date formats (e.g. DD-MM-YYYY or DD/MM/YYYY) to YYYY-MM-DD."""
        if not date_str:
            return None
            
        cleaned = DataCleaner.clean_whitespace(date_str)
        if cleaned in ["", "-", "none", "null", "pending"]:
            return None
            
        # Strip trailing timestamps if any
        cleaned = cleaned.split(" ")[0]
        
        # Try various date formats
        for fmt in ("%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d", "%d.%m.%Y"):
            try:
                dt = datetime.strptime(cleaned, fmt)
                return dt.strftime("%Y-%m-%d")
            except ValueError:
                continue
                
        return None

    @staticmethod
    def clean_name(name_str: Optional[str]) -> str:
        """Normalize names by removing common prefix titles, suffixes, and whitespace."""
        if not name_str:
            return ""
            
        name = DataCleaner.clean_whitespace(name_str)
        
        # Pattern to remove common legal/court titles at the start
        title_pattern = r'^(sri|smt|kum|kumari|dr|mr|mrs|ms|adv|advocate|justice|hon\'ble|government pleader for)\.?\s+'
        name = re.sub(title_pattern, '', name, flags=re.IGNORECASE)
        
        # Remove trailing designations or clean punctuation
        name = re.sub(r'\s*\(.*\)\s*$', '', name)  # removes trailing (Petitioner), (Advocate), etc.
        name = re.sub(r'[,.\s]+$', '', name)
        
        return name.strip().title()

    @staticmethod
    def clean_court_name(court_str: Optional[str]) -> str:
        """Normalize court and bench names for consistent grouping."""
        if not court_str:
            return "Unknown Court"
            
        court = DataCleaner.clean_whitespace(court_str)
        # Standardize common acronyms and naming variations
        court = re.sub(r'\b(hc|h\.c\.)\b', 'High Court', court, flags=re.IGNORECASE)
        court = re.sub(r'\b(dist|dist\.)\b', 'District', court, flags=re.IGNORECASE)
        
        return court.strip().title()

    @classmethod
    def clean_case_record(cls, raw_record: Dict[str, Any]) -> Dict[str, Any]:
        """Apply full cleaning transformations to a parsed case record dict."""
        clean_record = {}
        
        # Standard keys
        clean_record["cnr"] = cls.clean_whitespace(raw_record.get("cnr")).upper()
        clean_record["case_number"] = cls.clean_whitespace(raw_record.get("case_number")).upper()
        
        # Clean dates
        clean_record["filing_date"] = cls.parse_date(raw_record.get("filing_date_raw"))
        clean_record["registration_date"] = cls.parse_date(raw_record.get("registration_date_raw"))
        clean_record["disposal_date"] = cls.parse_date(raw_record.get("disposal_date_raw"))
        
        # Basic fields
        clean_record["current_stage"] = cls.clean_whitespace(raw_record.get("current_stage"))
        clean_record["status"] = cls.clean_whitespace(raw_record.get("status"))
        clean_record["court"] = cls.clean_court_name(raw_record.get("court"))
        clean_record["judge"] = cls.clean_name(raw_record.get("judge"))
        clean_record["case_category"] = cls.clean_whitespace(raw_record.get("case_category"))
        
        # Parties & Advocates
        clean_record["petitioner"] = cls.clean_name(raw_record.get("petitioner"))
        clean_record["petitioner_advocate"] = cls.clean_name(raw_record.get("petitioner_advocate"))
        clean_record["respondent"] = cls.clean_name(raw_record.get("respondent"))
        clean_record["respondent_advocate"] = cls.clean_name(raw_record.get("respondent_advocate"))
        
        # Nested structs
        clean_record["acts"] = [
            {
                "act": cls.clean_whitespace(a.get("act")),
                "section": cls.clean_whitespace(a.get("section"))
            }
            for a in raw_record.get("acts", [])
        ]
        
        clean_record["hearing_history"] = [
            {
                "hearing_date": cls.parse_date(h.get("hearing_date")),
                "stage": cls.clean_whitespace(h.get("stage")),
                "business": cls.clean_whitespace(h.get("business"))
            }
            for h in raw_record.get("hearing_history", [])
        ]
        
        clean_record["orders"] = [
            {
                "date": cls.parse_date(o.get("date")),
                "description": cls.clean_whitespace(o.get("description")),
                "pdf_url": cls.clean_whitespace(o.get("pdf_url"))
            }
            for o in raw_record.get("orders", [])
        ]
        
        # Preserving any unknown fields as metadata
        clean_record["metadata"] = {}
        for k, v in raw_record.items():
            if k not in clean_record and f"{k}_raw" not in raw_record and k != "cases":
                clean_record["metadata"][k] = v
                
        return clean_record
