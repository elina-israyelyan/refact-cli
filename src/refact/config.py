import os


class Colors:
    Question = "\033[95m"
    Thought = "\033[90m"
    Observation = "\033[90m"
    FinalAnswer = "\033[94m"
    End = "\033[0m"


REFACT_API_URL = os.getenv("REFACT_API_URL", "http://localhost:8000")
