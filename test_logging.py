import asyncio
from logging_utils import ForecastLogger


async def test_logging():
    # Initialize logger
    logger = ForecastLogger()

    # Test logging a question
    logger.log_question_start(
        "https://www.metaculus.com/questions/123", "Will X happen by 2025?"
    )

    # Test logging research results
    logger.log_research_result(
        "https://www.metaculus.com/questions/123", "Perplexity", True
    )

    # Test logging a failed research attempt
    logger.log_research_result(
        "https://www.metaculus.com/questions/123", "AskNews", False, "403 Forbidden"
    )

    # Test logging a forecast
    logger.log_forecast_result(
        "https://www.metaculus.com/questions/123",
        0.75,
        "Based on current trends and expert opinions...",
    )

    # Log summary
    logger.log_summary()


if __name__ == "__main__":
    asyncio.run(test_logging())
