import logging
from typing import Optional

logger = logging.getLogger(__name__)

class BrowserManager:
    """Manages browser automation using Playwright or Selenium with fallback strategies."""
    
    def __init__(self, driver_type: str = "selenium", headless: bool = True, timeout: int = 30):
        self.driver_type = driver_type
        self.headless = headless
        self.timeout = timeout
        
    def fetch_url(self, url: str) -> str:
        """Fetch URL using the chosen browser automation framework."""
        if self.driver_type == "playwright":
            return self._fetch_with_playwright(url)
        else:
            return self._fetch_with_selenium(url)

    def _fetch_with_playwright(self, url: str) -> str:
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            raise ImportError(
                "playwright is not installed. Run `pip install playwright` to enable playwright driver."
            )
            
        logger.info(f"Opening browser using Playwright to fetch: {url}")
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=self.headless)
                page = browser.new_page()
                page.goto(url, timeout=self.timeout * 1000)
                # Wait for tables or page content to load
                page.wait_for_load_state("networkidle")
                content = page.content()
                browser.close()
                return content
        except Exception as e:
            logger.error(f"Playwright execution failed: {e}")
            raise RuntimeError(f"Playwright failed to fetch {url}: {e}")

    def _fetch_with_selenium(self, url: str) -> str:
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options as ChromeOptions
            from selenium.webdriver.chrome.service import Service
        except ImportError:
            raise ImportError(
                "selenium is not installed. Run `pip install selenium` to enable selenium driver."
            )
            
        logger.info(f"Opening browser using Selenium to fetch: {url}")
        try:
            options = ChromeOptions()
            if self.headless:
                options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            
            # Use Chrome webdriver
            driver = webdriver.Chrome(options=options)
            driver.set_page_load_timeout(self.timeout)
            driver.get(url)
            # Give page time to load JavaScript elements
            import time
            time.sleep(3.0)
            content = driver.page_source
            driver.quit()
            return content
        except Exception as e:
            logger.error(f"Selenium execution failed: {e}")
            raise RuntimeError(f"Selenium failed to fetch {url}: {e}")
