import asyncio
import cmd
from typing import Any

import questionary
from aiohttp import ClientResponseError, ClientSession

from refact.config import Colors
from refact.refact_client.client import RefactClient
from refact.refact_client.models import RefactRequest


async def refact(refact_request: RefactRequest):
    try:
        async with ClientSession() as client_session:
            client = RefactClient(client_session)
            async for line in client.refact(refact_request):
                if line.startswith("Thought"):
                    print(Colors.Thought + line + Colors.End)
                    print(Colors.Thought + "-" * 9 + Colors.End)
                elif line.startswith("Observation"):
                    print(Colors.Observation + line + Colors.End)
                    print(Colors.Observation + "-" * 13 + Colors.End)
                elif line.startswith("Final answer"):
                    print(Colors.FinalAnswer + line + Colors.End)
    except ClientResponseError as e:
        print(f"Error: {e.message}")
    except Exception as e:
        print(f"Error: Unknown issue.")


def refact_cli_loop():
    print(
        "Welcome to the Refact CLI. Type your prompt to chat with the Refact agent or 'exit' to quit."
    )
    while True:
        query = questionary.text("refact>").ask()
        if query.strip().lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        asyncio.run(refact(RefactRequest(prompt=query)))
