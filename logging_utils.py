import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Optional


class ForecastLogger:
    def __init__(self, log_dir: str = "logs"):
        # Ensure we're using the repository's logs directory
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

        # Set up the main logger
        self.logger = logging.getLogger("forecast_bot")
        self.logger.setLevel(logging.INFO)

        # Create a unique log file for each run
        # Use GitHub Actions run number if available, otherwise use timestamp
        run_number = os.getenv("GITHUB_RUN_NUMBER", "local")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = self.log_dir / f"forecast_run_{run_number}_{timestamp}.log"

        # File handler with a more git-friendly format
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create formatter with a more git-friendly format
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        # Initialize counters
        self.question_count = 0
        self.success_count = 0
        self.failure_count = 0

        # Log the start of a new run
        self.logger.info(f"=== Starting new forecast run (Run #{run_number}) ===")
        if os.getenv("GITHUB_ACTIONS"):
            self.logger.info("Environment: GitHub Actions")
            self.logger.info(f"Repository: {os.getenv('GITHUB_REPOSITORY')}")
            self.logger.info(f"Workflow: {os.getenv('GITHUB_WORKFLOW')}")
            self.logger.info(f"Commit: {os.getenv('GITHUB_SHA')}")

    def log_question_start(self, question_url: str, question_text: str):
        """Log the start of processing a question."""
        self.question_count += 1
        self.logger.info(f"=== Question {self.question_count} ===")
        self.logger.info(f"URL: {question_url}")
        self.logger.info(f"Text: {question_text}")

    def log_research_result(
        self,
        question_url: str,
        search_engine: str,
        success: bool,
        error: Optional[str] = None,
    ):
        """Log the result of a research attempt."""
        if success:
            self.success_count += 1
            self.logger.info(f"Research: {search_engine} succeeded for {question_url}")
        else:
            self.failure_count += 1
            self.logger.warning(f"Research: {search_engine} failed for {question_url}")
            if error:
                self.logger.warning(f"Error details: {error}")

    def log_forecast_result(self, question_url: str, prediction: float, reasoning: str):
        """Log the forecast result for a question."""
        self.logger.info(f"=== Forecast Result ===")
        self.logger.info(f"URL: {question_url}")
        self.logger.info(f"Prediction: {prediction}")
        self.logger.info(f"Reasoning: {reasoning}")

    def log_summary(self):
        """Log a summary of the run."""
        self.logger.info("=== Run Summary ===")
        self.logger.info(f"Total questions: {self.question_count}")
        self.logger.info(f"Successful research: {self.success_count}")
        self.logger.info(f"Failed research: {self.failure_count}")
        if self.question_count > 0:
            success_rate = (self.success_count / self.question_count) * 100
            self.logger.info(f"Success rate: {success_rate:.2f}%")

    def get_logger(self) -> logging.Logger:
        """Get the logger instance."""
        return self.logger
