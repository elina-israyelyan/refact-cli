import os


class Colors:
    Neutral = "\033[90m"
    Question = "\033[95m"
    Thought = "\033[90m"
    Observation = "\033[90m"
    FinalAnswer = "\033[94m"
    Error = "\033[91m"
    End = "\033[0m"


REFACT_API_URL = os.getenv("REFACT_API_URL", "http://localhost:8000")
