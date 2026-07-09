import logging
from typing import Dict, Any, List
from analytics.analytics_engine import AnalyticsEngine
from validator.schema_validator import CaseRecordSchema

logger = logging.getLogger(__name__)

class ComparisonEngine:
    """Enables statistical comparison and benchmarking of two or more advocates."""
    
    @staticmethod
    def calculate_confidence_score(cases: List[CaseRecordSchema]) -> float:
        """Calculate a confidence score (0.0 to 100.0) based on profile completeness."""
        if not cases:
            return 0.0
            
        scores = []
        for case in cases:
            scores.append(case.calculate_completeness())
            
        avg_completeness = sum(scores) / len(scores) if scores else 0.0
        
        # Penalize if case count is very low (e.g. less than 3 cases limits historical trends reliability)
        volume_multiplier = min(len(cases) / 5.0, 1.0)
        
        # Score combines data completeness (80%) and volume weight (20%)
        weighted_score = (avg_completeness * 80.0) + (volume_multiplier * 20.0)
        return round(weighted_score, 1)

    @classmethod
    def compare_advocates(cls, name_a: str, cases_a: List[CaseRecordSchema], name_b: str, cases_b: List[CaseRecordSchema]) -> Dict[str, Any]:
        """Perform a detailed statistical comparison between two advocates."""
        stats_a = AnalyticsEngine.analyze_cases(cases_a)
        stats_b = AnalyticsEngine.analyze_cases(cases_b)
        
        conf_a = cls.calculate_confidence_score(cases_a)
        conf_b = cls.calculate_confidence_score(cases_b)
        
        # Top courts
        top_courts_a = sorted(stats_a.get("court_distribution", {}).items(), key=lambda x: x[1], reverse=True)[:3]
        top_courts_b = sorted(stats_b.get("court_distribution", {}).items(), key=lambda x: x[1], reverse=True)[:3]
        
        # Top categories (Practice areas)
        top_cat_a = sorted(stats_a.get("category_distribution", {}).items(), key=lambda x: x[1], reverse=True)[:3]
        top_cat_b = sorted(stats_b.get("category_distribution", {}).items(), key=lambda x: x[1], reverse=True)[:3]
        
        return {
            "lawyer_a": {
                "name": name_a,
                "confidence_score": conf_a,
                "total_cases": stats_a.get("total_cases", 0),
                "pending_cases": stats_a.get("pending_cases", 0),
                "disposed_cases": stats_a.get("disposed_cases", 0),
                "average_disposal_time_days": stats_a.get("average_disposal_time_days"),
                "top_courts": top_courts_a,
                "top_practice_areas": top_cat_a,
                "outcomes": stats_a.get("outcome_classification", {})
            },
            "lawyer_b": {
                "name": name_b,
                "confidence_score": conf_b,
                "total_cases": stats_b.get("total_cases", 0),
                "pending_cases": stats_b.get("pending_cases", 0),
                "disposed_cases": stats_b.get("disposed_cases", 0),
                "average_disposal_time_days": stats_b.get("average_disposal_time_days"),
                "top_courts": top_courts_b,
                "top_practice_areas": top_cat_b,
                "outcomes": stats_b.get("outcome_classification", {})
            },
            "comparison_summary": {
                "more_experienced_in_volume": name_a if len(cases_a) > len(cases_b) else (name_b if len(cases_b) > len(cases_a) else "Equal"),
                "faster_disposal_time": name_a if (stats_a.get("average_disposal_time_days") or 999999) < (stats_b.get("average_disposal_time_days") or 999999) else name_b
            }
        }
