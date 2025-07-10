import questionary

from refact.commands.act import act_cli_loop
from refact.commands.reason import reason_cli_loop
from refact.commands.refact import refact_cli_loop


def main():
    mode = questionary.select(
        "Which CLI mode do you want to start?",
        choices=[
            {"name": "Refact", "value": "refact"},
            {"name": "Reason", "value": "reason"},
            {"name": "Act", "value": "act"},
        ],
    ).ask()

    if mode == "refact":
        from refact.commands.refact import refact_cli_loop

        refact_cli_loop()
    elif mode == "reason":
        from refact.commands.reason import reason_cli_loop

        reason_cli_loop()
    elif mode == "act":
        from refact.commands.act import act_cli_loop

        act_cli_loop()


if __name__ == "__main__":
    main()
