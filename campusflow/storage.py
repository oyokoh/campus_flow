import json
from pathlib import Path


def save_tickets(tickets, filepath="data/tickets.json"):
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4)


def load_tickets(filepath="data/tickets.json"):
    path = Path(filepath)

    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            tickets = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Ticket data in {filepath} is not valid JSON."
        ) from error

    if not isinstance(tickets, list):
        raise ValueError("Ticket data must contain a JSON list.")

    return tickets


import json
from pathlib import Path


def save_tickets(tickets, filepath="data/tickets.json"):
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4)


def load_tickets(filepath="data/tickets.json"):
    path = Path(filepath)

    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            tickets = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Ticket data in {filepath} is not valid JSON."
        ) from error

    if not isinstance(tickets, list):
        raise ValueError("Ticket data must contain a JSON list.")

    return tickets
1