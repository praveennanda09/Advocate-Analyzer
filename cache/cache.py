import sqlite3
import time
from pathlib import Path
from typing import Optional

class ResponseCache:
    """A SQLite-based caching layer for raw HTML request content."""
    
    def __init__(self, db_path: str = "data/request_cache.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()
        
    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS cache (
                    url TEXT PRIMARY KEY,
                    content TEXT,
                    timestamp REAL,
                    ttl INTEGER
                )
            """)
            conn.commit()

    def get(self, url: str) -> Optional[str]:
        """Retrieve cached content for a URL if not expired."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT content, timestamp, ttl FROM cache WHERE url = ?", (url,))
            row = cursor.fetchone()
            if not row:
                return None
                
            content, timestamp, ttl = row
            # If ttl is -1, it never expires
            if ttl != -1 and (time.time() - timestamp) > ttl:
                self.delete(url)
                return None
                
            return content

    def set(self, url: str, content: str, ttl: int = 86400):
        """Cache HTML content for a specific URL."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO cache (url, content, timestamp, ttl) VALUES (?, ?, ?, ?)",
                (url, content, time.time(), ttl)
            )
            conn.commit()

    def delete(self, url: str):
        """Remove a cached URL."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM cache WHERE url = ?", (url,))
            conn.commit()

    def clear(self):
        """Clear all cached entries."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM cache")
            conn.commit()
