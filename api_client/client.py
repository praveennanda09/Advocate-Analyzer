import random
import time
import logging
from typing import Dict, Any, Optional
import httpx
from cache.cache import ResponseCache

logger = logging.getLogger(__name__)

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
]

class HTTPClient:
    """HTTP Client that handles requests with caching, headers, and rate limits."""
    
    def __init__(self, cache: Optional[ResponseCache] = None, rate_limit_delay: float = 3.0, timeout: int = 30):
        self.cache = cache
        self.rate_limit_delay = rate_limit_delay
        self.timeout = timeout
        self.last_request_time = 0.0

    def _get_headers(self) -> Dict[str, str]:
        return {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1"
        }

    def fetch(self, url: str, use_cache: bool = True, cache_ttl: int = 86400) -> str:
        """Fetch the content of a URL, utilizing cache if configured and available."""
        if use_cache and self.cache:
            cached_content = self.cache.get(url)
            if cached_content:
                logger.debug(f"Cache hit for URL: {url}")
                return cached_content
        
        # Respect rate limits
        elapsed = time.time() - self.last_request_time
        if elapsed < self.rate_limit_delay:
            time.sleep(self.rate_limit_delay - elapsed)
            
        logger.info(f"Fetching URL: {url}")
        self.last_request_time = time.time()
        
        try:
            with httpx.Client(headers=self._get_headers(), timeout=self.timeout, follow_redirects=True) as client:
                response = client.get(url)
                # eCourts sites sometimes block and return 403, raising an exception allows browser fallback
                response.raise_for_status()
                content = response.text
                
                if self.cache:
                    self.cache.set(url, content, ttl=cache_ttl)
                    
                return content
        except httpx.HTTPStatusError as e:
            logger.warning(f"HTTP error fetching {url}: {e.response.status_code}")
            raise e
        except Exception as e:
            logger.error(f"Network error fetching {url}: {e}")
            raise e
