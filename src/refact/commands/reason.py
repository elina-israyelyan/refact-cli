import asyncio
from typing import Any

import questionary
from aiohttp import ClientResponseError, ClientSession

from refact.config import Colors
from refact.refact_client.client import RefactClient
from refact.refact_client.models import ReasonRequest


async def reason(reason_request: ReasonRequest):
    try:
        async with ClientSession() as client_session:
            client = RefactClient(client_session)
            response = await client.reason(reason_request)
            print(Colors.FinalAnswer + response.text + Colors.End)
    except ClientResponseError as e:
        print(f"Error: {e.message}")
    except Exception as e:
        print(f"Error: Unknown issue.")


def reason_cli_loop():
    print(
        "Welcome to the Reason CLI. Type your prompt to chat with the Reason agent or 'exit' to quit."
    )
    while True:
        query = questionary.text("reason>").ask()
        if query.strip().lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        asyncio.run(reason(ReasonRequest(prompt=query)))
