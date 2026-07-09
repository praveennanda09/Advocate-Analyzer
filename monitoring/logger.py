import logging
import os
import json
import time
from pathlib import Path
from typing import Dict, Any

def setup_logger(log_level: str = "INFO", log_file: str = "data/scraper.log"):
    """Configure system-wide logging formatting and targets."""
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    # Root logger
    root = logging.getLogger()
    root.setLevel(numeric_level)
    
    # Clear existing handlers
    if root.handlers:
        root.handlers.clear()
        
    # File handler
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)
    root.addHandler(file_handler)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)

class CrawlMetricsTracker:
    """Collects and serializes operational metrics for monitoring dashboards."""
    
    def __init__(self, metrics_file: str = "data/metrics.json"):
        self.metrics_file = Path(metrics_file)
        self.metrics_file.parent.mkdir(parents=True, exist_ok=True)
        self.reset()
        
    def reset(self):
        self.start_time = time.time()
        self.pages_scraped = 0
        self.failed_requests = 0
        self.cases_parsed = 0
        self.database_writes = 0
        self.errors = []

    def log_scrape(self, success: bool = True):
        if success:
            self.pages_scraped += 1
        else:
            self.failed_requests += 1

    def log_case_parsed(self):
        self.cases_parsed += 1

    def log_db_write(self):
        self.database_writes += 1

    def log_error(self, err_msg: str):
        self.errors.append({
            "timestamp": time.time(),
            "message": err_msg
        })

    def save(self):
        duration = time.time() - self.start_time
        metrics = {
            "timestamp": datetime.now().isoformat(),
            "elapsed_seconds": round(duration, 2),
            "pages_scraped": self.pages_scraped,
            "failed_requests": self.failed_requests,
            "cases_parsed": self.cases_parsed,
            "database_writes": self.database_writes,
            "success_rate": round(
                (self.pages_scraped / (self.pages_scraped + self.failed_requests)) * 100
                if (self.pages_scraped + self.failed_requests) > 0 else 0,
                2
            ),
            "errors": self.errors
        }
        
        with open(self.metrics_file, "w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=4)
            
from datetime import datetime
