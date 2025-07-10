import asyncio

import questionary
from aiohttp import ClientResponseError, ClientSession

from refact.config import Colors
from refact.refact_client.client import RefactClient
from refact.refact_client.models import (
    ActRequest,
    MathActionsDivide,
    MathActionsMultiply,
    MathActionsPower,
    MathActionsSubtract,
    MathActionsSum,
    SearchActionsLookup,
    SearchActionsSearch,
)


async def act(action: ActRequest):
    try:
        async with ClientSession() as client_session:
            client = RefactClient(client_session)
            response = await client.act(action)
            print(Colors.FinalAnswer + str(response.result) + Colors.End)
    except ClientResponseError as e:
        print(Colors.Error + f"Error: {e.message}" + Colors.End)
    except Exception as e:
        print(Colors.Error + f"Error: Unknown issue." + Colors.End)


def act_cli_loop():
    actions = [
        {"name": "multiply", "value": "multiply"},
        {"name": "power", "value": "power"},
        {"name": "divide", "value": "divide"},
        {"name": "subtract", "value": "subtract"},
        {"name": "sum", "value": "sum"},
        {"name": "lookup", "value": "lookup"},
        {"name": "search", "value": "search"},
        {"name": "Exit", "value": "exit"},
    ]
    while True:
        action = questionary.select("Choose an action:", choices=actions).ask()
        if action == "exit":
            print("Goodbye!")
            break
        if action in ["multiply", "power", "divide", "subtract", "sum"]:
            a = questionary.text(
                "Enter value for a:",
                validate=lambda val: val.replace(".", "", 1).isdigit(),
            ).ask()
            b = questionary.text(
                "Enter value for b:",
                validate=lambda val: val.replace(".", "", 1).isdigit(),
            ).ask()
            a, b = float(a), float(b)
            if action == "multiply":
                asyncio.run(act(ActRequest(action=MathActionsMultiply(a=a, b=b))))
            elif action == "power":
                asyncio.run(act(ActRequest(action=MathActionsPower(a=a, b=b))))
            elif action == "divide":
                asyncio.run(act(ActRequest(action=MathActionsDivide(a=a, b=b))))
            elif action == "subtract":
                asyncio.run(act(ActRequest(action=MathActionsSubtract(a=a, b=b))))
            elif action == "sum":
                asyncio.run(act(ActRequest(action=MathActionsSum(a=a, b=b))))
        elif action == "lookup":
            entity = questionary.text("Enter entity:").ask()
            string = questionary.text("Enter string:").ask()
            asyncio.run(
                act(
                    ActRequest(action=SearchActionsLookup(entity=entity, string=string))
                )
            )
        elif action == "search":
            entity = questionary.text("Enter entity:").ask()
            asyncio.run(act(ActRequest(action=SearchActionsSearch(entity=entity))))
