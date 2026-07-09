from pathlib import Path

TEST_QUERIES_FILE = Path("src/evaluation/test_queries.csv")

REPORTS_DIR = Path("reports/evaluation")
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

RETRIEVAL_REPORT_FILE = REPORTS_DIR / "retrieval_evaluation_report.csv"