from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Dict, Any
import re

class ActSchema(BaseModel):
    act: str = Field(..., description="The name of the governing act")
    section: str = Field(..., description="The specific section of the act")

class HearingSchema(BaseModel):
    hearing_date: Optional[str] = Field(None, description="ISO formatted hearing date YYYY-MM-DD")
    stage: str = Field(..., description="Stage of the case during the hearing")
    business: str = Field(..., description="Details of business conducted")

class OrderSchema(BaseModel):
    date: Optional[str] = Field(None, description="ISO formatted date of order YYYY-MM-DD")
    description: str = Field(..., description="Brief description of the order")
    pdf_url: str = Field("", description="URL path to view/download order document")

class CaseRecordSchema(BaseModel):
    cnr: str = Field(..., description="Unique Case Number Record (16-character string)")
    case_number: str = Field(..., description="Standard case identifier")
    filing_date: Optional[str] = Field(None, description="ISO format filing date YYYY-MM-DD")
    registration_date: Optional[str] = Field(None, description="ISO format registration date YYYY-MM-DD")
    disposal_date: Optional[str] = Field(None, description="ISO format disposal date YYYY-MM-DD")
    current_stage: str = Field("", description="Current status/stage of case")
    status: str = Field(..., description="Pending or Disposed status description")
    court: str = Field(..., description="Name of the court complex")
    judge: str = Field("", description="Presiding judge")
    case_category: str = Field("", description="Categorization of case")
    petitioner: str = Field(..., description="Name of the petitioner/plaintiff")
    petitioner_advocate: str = Field("", description="Petitioner advocate name")
    respondent: str = Field(..., description="Name of the respondent/defendant")
    respondent_advocate: str = Field("", description="Respondent advocate name")
    acts: List[ActSchema] = Field(default_factory=list)
    hearing_history: List[HearingSchema] = Field(default_factory=list)
    orders: List[OrderSchema] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

    @field_validator("cnr")
    @classmethod
    def validate_cnr(cls, v: str) -> str:
        # Match standard eCourts CNR structure (16 alphanumeric characters)
        if not re.match(r'^[A-Z0-9]{16}$', v):
            raise ValueError(f"CNR number must be exactly 16 alphanumeric characters. Got: '{v}'")
        return v

    def calculate_completeness(self) -> float:
        """Calculate a completeness score (0.0 to 1.0) based on critical legal fields."""
        critical_fields = [
            self.cnr,
            self.case_number,
            self.filing_date,
            self.court,
            self.judge,
            self.petitioner,
            self.respondent,
            self.petitioner_advocate or self.respondent_advocate
        ]
        filled_count = sum(1 for field in critical_fields if field)
        return float(filled_count) / len(critical_fields)

class AdvocateProfileSchema(BaseModel):
    name: str = Field(..., description="Full name of the advocate")
    registration_number: str = Field(..., description="Bar registration number")
    bar_council: str = Field("", description="Governing bar council")
    primary_courts: str = Field("", description="Primary practicing courts")
    cases: List[CaseRecordSchema] = Field(default_factory=list)
