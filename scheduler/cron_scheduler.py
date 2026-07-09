import time
import logging
import threading
from typing import Callable

logger = logging.getLogger(__name__)

class SimpleScheduler:
    """Manages scheduled execution of the crawling and indexing tasks."""
    
    def __init__(self, interval_seconds: int, task: Callable[[], None]):
        self.interval = interval_seconds
        self.task = task
        self.stop_event = threading.Event()
        self.thread: Optional[threading.Thread] = None

    def start(self):
        """Start the scheduler thread."""
        if self.thread is not None and self.thread.is_alive():
            logger.warning("Scheduler thread is already running.")
            return
            
        self.stop_event.clear()
        self.thread = threading.Thread(target=self._run_loop, daemon=True)
        self.thread.start()
        logger.info(f"Scheduler started. Task will execute every {self.interval} seconds.")

    def _run_loop(self):
        while not self.stop_event.is_set():
            logger.info("Scheduler triggering task execution...")
            try:
                self.task()
            except Exception as e:
                logger.error(f"Error in scheduler task execution: {e}")
                
            # Sleep in increments to check stop_event frequently
            slept = 0
            while slept < self.interval:
                if self.stop_event.is_set():
                    break
                time.sleep(1)
                slept += 1

    def stop(self):
        """Signal the scheduler to stop execution and wait for completion."""
        if self.thread is None:
            return
            
        logger.info("Stopping scheduler...")
        self.stop_event.set()
        self.thread.join(timeout=5)
        logger.info("Scheduler successfully stopped.")
        self.thread = None
        
from typing import Optional
