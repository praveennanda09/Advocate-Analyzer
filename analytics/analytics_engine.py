from datetime import datetime
import logging
from typing import Dict, Any, List, Optional
from validator.schema_validator import CaseRecordSchema

logger = logging.getLogger(__name__)

class AnalyticsEngine:
    """Computes evidence-backed statistical analytics on legal case records."""
    
    @staticmethod
    def classify_outcome(case: CaseRecordSchema) -> Dict[str, str]:
        """Classify case outcomes without fabricating wins or losses.
        
        If evidence does not explicitly document the final ruling type,
        classifies as 'Unknown Outcome' with reasoning.
        """
        status_lower = case.status.lower()
        stage_lower = case.current_stage.lower()
        
        # Check if the case is still pending
        if "pending" in status_lower or "pending" in stage_lower:
            return {"outcome": "Pending", "reason": "Case is currently active."}
            
        # Parse text evidence in status or hearings
        evidence_text = f"{case.status} "
        for hearing in case.hearing_history:
            evidence_text += f"{hearing.business} "
            
        evidence_text_lower = evidence_text.lower()
        
        if "dismissed for default" in evidence_text_lower or "dismissed for non-prosecution" in evidence_text_lower:
            return {
                "outcome": "Dismissed for Default",
                "reason": "Case was dismissed due to the absence of the plaintiff or failure to prosecute."
            }
        elif "allowed" in evidence_text_lower or "decreed" in evidence_text_lower or "suit decreed" in evidence_text_lower:
            return {
                "outcome": "Allowed / Decreed",
                "reason": f"Case record explicitly states: 'Allowed' or 'Decreed'."
            }
        elif "withdrawn" in evidence_text_lower:
            return {
                "outcome": "Withdrawn",
                "reason": "Petitioner chose to withdraw the matter."
            }
        elif "settled" in evidence_text_lower or "compromised" in evidence_text_lower or "lok adalat" in evidence_text_lower:
            return {
                "outcome": "Settled / Compromised",
                "reason": "Case was settled through alternative dispute resolution or mutual compromise."
            }
        elif "quashed" in evidence_text_lower:
            return {
                "outcome": "Allowed / Quashed",
                "reason": "Court quashed the impugned order or assessment."
            }
        elif "dismissed" in evidence_text_lower:
            return {
                "outcome": "Dismissed",
                "reason": "Case was dismissed on merits."
            }
            
        return {
            "outcome": "Unknown Outcome",
            "reason": f"Disposed status is '{case.status}', but no explicit text confirms if it was decreed, dismissed on merits, settled, or withdrawn."
        }

    @classmethod
    def analyze_cases(cls, cases: List[CaseRecordSchema]) -> Dict[str, Any]:
        """Compute aggregate metrics and trends over a list of case records."""
        total_cases = len(cases)
        if total_cases == 0:
            return {"total_cases": 0}
            
        pending_count = 0
        disposed_count = 0
        
        court_dist: Dict[str, int] = {}
        judge_dist: Dict[str, int] = {}
        category_dist: Dict[str, int] = {}
        opponent_dist: Dict[str, int] = {}
        
        durations = []
        outcomes: Dict[str, int] = {}
        filing_by_year: Dict[int, int] = {}
        disposal_by_year: Dict[int, int] = {}
        
        for case in cases:
            # 1. Pending vs Disposed
            is_pending = "pending" in case.status.lower() or "pending" in case.current_stage.lower()
            if is_pending:
                pending_count += 1
            else:
                disposed_count += 1
                
            # 2. Distributions
            court_dist[case.court] = court_dist.get(case.court, 0) + 1
            if case.judge:
                judge_dist[case.judge] = judge_dist.get(case.judge, 0) + 1
            if case.case_category:
                category_dist[case.case_category] = category_dist.get(case.case_category, 0) + 1
                
            opp_adv = case.respondent_advocate
            # If the advocate we track is the respondent advocate, then opponent is petitioner advocate
            # For general statistics, we look at respondent_advocate if present
            if opp_adv:
                opponent_dist[opp_adv] = opponent_dist.get(opp_adv, 0) + 1
                
            # 3. Timelines & Durations
            if case.filing_date:
                try:
                    f_dt = datetime.strptime(case.filing_date, "%Y-%m-%d")
                    filing_by_year[f_dt.year] = filing_by_year.get(f_dt.year, 0) + 1
                    
                    if case.disposal_date:
                        d_dt = datetime.strptime(case.disposal_date, "%Y-%m-%d")
                        disposal_by_year[d_dt.year] = disposal_by_year.get(d_dt.year, 0) + 1
                        
                        duration = (d_dt - f_dt).days
                        if duration >= 0:
                            durations.append(duration)
                except Exception as e:
                    logger.debug(f"Failed parsing dates for duration calculation: {e}")
                    
            # 4. Outcomes
            outcome_res = cls.classify_outcome(case)
            out_label = outcome_res["outcome"]
            outcomes[out_label] = outcomes.get(out_label, 0) + 1
            
        avg_disposal = sum(durations) / len(durations) if durations else None
        
        return {
            "total_cases": total_cases,
            "pending_cases": pending_count,
            "disposed_cases": disposed_count,
            "court_distribution": court_dist,
            "judge_frequency": judge_dist,
            "category_distribution": category_dist,
            "opponent_frequency": opponent_dist,
            "filing_trends_yearly": filing_by_year,
            "disposal_trends_yearly": disposal_by_year,
            "average_disposal_time_days": avg_disposal,
            "outcome_classification": outcomes,
            "case_durations_raw": durations
        }
