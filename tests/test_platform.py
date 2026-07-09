import pytest
import tempfile
import os
from pathlib import Path

from config.config import load_config, AppConfig
from cache.cache import ResponseCache
from scraper.scraper import GenericScraper
from api_client.client import HTTPClient
from browser.browser_manager import BrowserManager
from parser.html_parser import HTMLParser
from cleaner.data_cleaner import DataCleaner
from validator.schema_validator import CaseRecordSchema, ActSchema, HearingSchema, OrderSchema
from storage.storage_manager import SQLiteRepository, JSONLRepository, ParquetRepository
from indexing.chunker import Chunker
from embeddings.embeddings_manager import EmbeddingsManager, MockEmbeddings
from vectorstore.store import FAISSStore
from llm.llm_client import LLMClientManager, MockLLMClient
from rag.rag_pipeline import RAGPipeline
from analytics.analytics_engine import AnalyticsEngine
from comparison.comparison_engine import ComparisonEngine
from scraper.mock_data import LAWYER_PROFILES, CASE_DETAILS

def test_config_load():
    """Verify default configurations load correctly."""
    config = load_config()
    assert isinstance(config, AppConfig)
    assert config.crawler.mode in ["mock", "http", "browser"]
    assert config.storage.base_dir == "data"

def test_cache_operations():
    """Test SQLite-based request caching."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        db_path = os.path.join(tmp_dir, "cache.db")
        cache = ResponseCache(db_path)
        
        url = "https://ecourtsindia.com/lawyer/test"
        html = "<html><body>Test Advocate</body></html>"
        
        # Get nonexistent
        assert cache.get(url) is None
        
        # Set and get
        cache.set(url, html, ttl=60)
        assert cache.get(url) == html
        
        # Clear
        cache.clear()
        assert cache.get(url) is None

def test_html_parsing():
    """Verify HTML parsing of advocate profiles and cases."""
    profile_html = LAWYER_PROFILES["kuchi-rajeswara-sastry"]
    profile_data = HTMLParser.parse_lawyer_profile(profile_html)
    
    assert profile_data["name"] == "Kuchi Rajeswara Sastry"
    assert profile_data["registration_number"] == "AP/1042/1971"
    assert len(profile_data["cases"]) == 3
    
    case_html = CASE_DETAILS["APGD050012342021"]
    case_data = HTMLParser.parse_case_details(case_html)
    
    assert case_data["cnr"] == "APGD050012342021"
    assert case_data["case_number"] == "O.S. 104/2021"
    assert case_data["filing_date_raw"] == "15-04-2021"
    assert case_data["judge"] == "Sri K. Sree Rama Murthy"
    assert len(case_data["acts"]) == 1
    assert case_data["acts"][0]["act"] == "Code of Civil Procedure, 1908"
    assert len(case_data["hearing_history"]) == 3

def test_data_cleaning():
    """Verify name cleaning, date standardization, and case cleaner outputs."""
    # Date parsing
    assert DataCleaner.parse_date("15-04-2021") == "2021-04-15"
    assert DataCleaner.parse_date("12/05/2022") == "2022-05-12"
    assert DataCleaner.parse_date("-") is None
    
    # Name cleaning
    assert DataCleaner.clean_name("Sri K. Sree Rama Murthy") == "K. Sree Rama Murthy"
    assert DataCleaner.clean_name("Smt. M. Rajani (Petitioner)") == "M. Rajani"
    
    # Court cleaning
    assert DataCleaner.clean_court_name("dist court mumbai") == "District Court Mumbai"
    
    # Complete case record cleaning
    raw_case = HTMLParser.parse_case_details(CASE_DETAILS["APGD050012342021"])
    clean_case = DataCleaner.clean_case_record(raw_case)
    
    assert clean_case["cnr"] == "APGD050012342021"
    assert clean_case["filing_date"] == "2021-04-15"
    assert clean_case["registration_date"] == "2021-04-18"
    assert clean_case["disposal_date"] == "2023-10-12"
    assert clean_case["judge"] == "K. Sree Rama Murthy"
    assert clean_case["petitioner_advocate"] == "Kuchi Rajeswara Sastry"

def test_pydantic_validation():
    """Test validator schemas and validation rules."""
    raw_case = HTMLParser.parse_case_details(CASE_DETAILS["APGD050012342021"])
    clean_case = DataCleaner.clean_case_record(raw_case)
    
    # Successful validation
    validated = CaseRecordSchema(**clean_case)
    assert validated.cnr == "APGD050012342021"
    assert validated.calculate_completeness() > 0.8
    
    # CNR Validation failure
    clean_case["cnr"] = "INVALID_CNR"
    with pytest.raises(ValueError):
        CaseRecordSchema(**clean_case)

def test_storage_backends():
    """Test saving and loading records across SQLite and Parquet repositories."""
    raw_case = HTMLParser.parse_case_details(CASE_DETAILS["APGD050012342021"])
    clean_case = DataCleaner.clean_case_record(raw_case)
    validated = CaseRecordSchema(**clean_case)
    
    with tempfile.TemporaryDirectory() as tmp_dir:
        # 1. Test SQLite Repo
        db_path = os.path.join(tmp_dir, "test_kb.db")
        db_repo = SQLiteRepository(db_path)
        
        db_repo.save_case(validated)
        retrieved = db_repo.get_case(validated.cnr)
        
        assert retrieved is not None
        assert retrieved.cnr == validated.cnr
        assert retrieved.case_number == validated.case_number
        assert len(retrieved.acts) == len(validated.acts)
        assert len(retrieved.hearing_history) == len(validated.hearing_history)
        
        # Test List
        all_cases = db_repo.list_cases()
        assert len(all_cases) == 1
        
        # 2. Test Parquet Repo
        parquet_path = os.path.join(tmp_dir, "test_cases.parquet")
        parquet_repo = ParquetRepository(parquet_path)
        parquet_repo.save_all(all_cases)
        
        df = parquet_repo.load_dataframe()
        assert not df.empty
        assert df.iloc[0]["cnr"] == validated.cnr
        assert df.iloc[0]["num_hearings"] == 3

def test_analytics_engine():
    """Verify metrics extraction, case durations, and outcome classifications."""
    cases = []
    for cnr in ["APGD050012342021", "APGD050024682022"]:
        raw_case = HTMLParser.parse_case_details(CASE_DETAILS[cnr])
        clean_case = DataCleaner.clean_case_record(raw_case)
        cases.append(CaseRecordSchema(**clean_case))
        
    stats = AnalyticsEngine.analyze_cases(cases)
    
    assert stats["total_cases"] == 2
    assert stats["pending_cases"] == 1
    assert stats["disposed_cases"] == 1
    assert stats["court_distribution"]["Senior Civil Court, Amalapuram"] == 1
    
    # Check outcomes classification
    outcome_apgd = AnalyticsEngine.classify_outcome(cases[0])
    assert outcome_apgd["outcome"] == "Allowed / Decreed"
    
    outcome_pending = AnalyticsEngine.classify_outcome(cases[1])
    assert outcome_pending["outcome"] == "Pending"

def test_comparison_engine():
    """Verify narrative advocate comparative analytics."""
    cases_sastry = []
    for cnr in ["APGD050012342021", "APGD050024682022"]:
        raw_case = HTMLParser.parse_case_details(CASE_DETAILS[cnr])
        clean_case = DataCleaner.clean_case_record(raw_case)
        cases_sastry.append(CaseRecordSchema(**clean_case))
        
    cases_doe = []
    raw_case_doe = HTMLParser.parse_case_details(CASE_DETAILS["MHMC010098762020"])
    clean_case_doe = DataCleaner.clean_case_record(raw_case_doe)
    cases_doe.append(CaseRecordSchema(**clean_case_doe))
    
    comp = ComparisonEngine.compare_advocates("kuchi-rajeswara-sastry", cases_sastry, "john-doe", cases_doe)
    
    assert comp["lawyer_a"]["total_cases"] == 2
    assert comp["lawyer_b"]["total_cases"] == 1
    assert comp["comparison_summary"]["more_experienced_in_volume"] == "kuchi-rajeswara-sastry"

def test_rag_pipeline():
    """Verify document chunking, mock embeddings indexing, search, and QA RAG flow."""
    cases = []
    raw_case = HTMLParser.parse_case_details(CASE_DETAILS["APGD050012342021"])
    clean_case = DataCleaner.clean_case_record(raw_case)
    cases.append(CaseRecordSchema(**clean_case))
    
    # 1. Chunker
    chunks = Chunker.chunk_all_cases(cases)
    assert len(chunks) == 4  # Summary, Acts, Hearings, Orders
    
    # 2. Embedding & Vector Store
    embeddings = MockEmbeddings()
    vector_store = FAISSStore(embeddings)
    vector_store.add_documents(chunks)
    
    # Test search
    search_results = vector_store.similarity_search("Garapati partition suit Amalapuram", k=1)
    assert len(search_results) == 1
    assert search_results[0][0]["metadata"]["cnr"] == "APGD050012342021"
    
    # 3. LLM QA Flow
    llm = MockLLMClient()
    pipeline = RAGPipeline(vector_store, llm)
    result = pipeline.answer_query("How many cases did Kuchi Rajeswara Sastry handle?", k=1)
    
    assert "3 cases" in result["answer"]
    assert len(result["sources"]) == 1

