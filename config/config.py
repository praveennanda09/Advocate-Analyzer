import os
from pathlib import Path
from typing import Any, Dict
import yaml
from pydantic import BaseModel, Field

# Default path config.yaml
DEFAULT_CONFIG_PATH = Path(__file__).parent / "config.yaml"

class CrawlerConfig(BaseModel):
    mode: str = "mock"
    default_target: str = "https://ecourtsindia.com/lawyer/kuchi-rajeswara-sastry"
    rate_limit_delay: float = 3.0
    max_depth: int = 2
    timeout: int = 30
    cache_ttl: int = 86400

class StorageConfig(BaseModel):
    base_dir: str = "data"
    db_path: str = "data/legal_kb.db"
    json_path: str = "data/raw_cases.jsonl"
    parquet_path: str = "data/analytics_cases.parquet"

class RagConfig(BaseModel):
    vector_db: str = "faiss"
    vector_db_dir: str = "data/vector_store"
    chunk_size: int = 500
    chunk_overlap: int = 50
    embeddings_provider: str = "mock"
    llm_provider: str = "mock"
    llm_model: str = "gemini-1.5-flash"
    temperature: float = 0.2

class MonitoringConfig(BaseModel):
    log_level: str = "INFO"
    log_file: str = "data/scraper.log"

class AppConfig(BaseModel):
    crawler: CrawlerConfig = Field(default_factory=CrawlerConfig)
    storage: StorageConfig = Field(default_factory=StorageConfig)
    rag: RagConfig = Field(default_factory=RagConfig)
    monitoring: MonitoringConfig = Field(default_factory=MonitoringConfig)

def load_config(config_path: Path = DEFAULT_CONFIG_PATH) -> AppConfig:
    """Loads configuration from YAML file, merges environment overrides, and returns AppConfig."""
    if not config_path.exists():
        # Return default config if file doesn't exist
        return AppConfig()
    
    with open(config_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
        
    config = AppConfig(**data)
    
    # Ensure directories exist
    os.makedirs(config.storage.base_dir, exist_ok=True)
    os.makedirs(Path(config.storage.db_path).parent, exist_ok=True)
    os.makedirs(Path(config.storage.json_path).parent, exist_ok=True)
    os.makedirs(Path(config.storage.parquet_path).parent, exist_ok=True)
    os.makedirs(config.rag.vector_db_dir, exist_ok=True)
    os.makedirs(Path(config.monitoring.log_file).parent, exist_ok=True)
    
    return config
