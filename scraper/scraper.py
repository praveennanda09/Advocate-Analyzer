import logging
from typing import Optional
from config.config import AppConfig
from api_client.client import HTTPClient
from browser.browser_manager import BrowserManager
from scraper.mock_data import LAWYER_PROFILES, CASE_DETAILS

logger = logging.getLogger(__name__)

class GenericScraper:
    """High-level scraper coordinator that handles mock, direct HTTP, or browser-based crawling."""
    
    def __init__(self, config: AppConfig, http_client: HTTPClient, browser_manager: BrowserManager):
        self.config = config
        self.http_client = http_client
        self.browser_manager = browser_manager
        self.mode = config.crawler.mode.lower()

    def get_lawyer_profile(self, name_or_url: str) -> str:
        """Fetch lawyer profile page by name identifier or full URL."""
        if self.mode == "mock":
            # Extract key/slug from URL or name
            key = name_or_url.split("/")[-1] if "/" in name_or_url else name_or_url
            if key not in LAWYER_PROFILES:
                logger.warning(f"Lawyer profile '{key}' not found in mock database. Defaulting to 'kuchi-rajeswara-sastry'")
                key = "kuchi-rajeswara-sastry"
            return LAWYER_PROFILES[key]
            
        # For live modes: ensure we have a URL
        url = name_or_url
        if not url.startswith("http"):
            url = f"https://ecourtsindia.com/lawyer/{name_or_url}"

        if self.mode == "http":
            try:
                return self.http_client.fetch(url, use_cache=True, cache_ttl=self.config.crawler.cache_ttl)
            except Exception as e:
                logger.warning(f"HTTP fetch failed for {url}, attempting browser fallback: {e}")
                # Fallback to browser execution
                return self.browser_manager.fetch_url(url)
                
        elif self.mode == "browser":
            try:
                return self.browser_manager.fetch_url(url)
            except Exception as e:
                logger.error(f"Browser execution failed for {url}, attempting HTTP fallback: {e}")
                # Fallback to standard HTTP
                return self.http_client.fetch(url, use_cache=True, cache_ttl=self.config.crawler.cache_ttl)
        else:
            raise ValueError(f"Unsupported scraping mode: {self.mode}")

    def get_case_details(self, cnr_number: str) -> str:
        """Fetch case details by CNR number."""
        if self.mode == "mock":
            if cnr_number not in CASE_DETAILS:
                raise ValueError(f"Case with CNR '{cnr_number}' not found in mock database.")
            return CASE_DETAILS[cnr_number]

        url = f"https://ecourtsindia.com/cnr/{cnr_number}"
        
        if self.mode == "http":
            try:
                return self.http_client.fetch(url, use_cache=True, cache_ttl=self.config.crawler.cache_ttl)
            except Exception as e:
                logger.warning(f"HTTP fetch failed for case {cnr_number}, attempting browser fallback: {e}")
                return self.browser_manager.fetch_url(url)
                
        elif self.mode == "browser":
            try:
                return self.browser_manager.fetch_url(url)
            except Exception as e:
                logger.error(f"Browser execution failed for case {cnr_number}, attempting HTTP fallback: {e}")
                return self.http_client.fetch(url, use_cache=True, cache_ttl=self.config.crawler.cache_ttl)
        else:
            raise ValueError(f"Unsupported scraping mode: {self.mode}")
