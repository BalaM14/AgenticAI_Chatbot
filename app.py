import os
import sys

# Ensure src/ is discoverable
sys.path.append(os.path.abspath("."))

from src.langgrapghagenticai.main import load_langgrapgh_agentic_app


if __name__ == "__main__":
    load_langgrapgh_agentic_app()