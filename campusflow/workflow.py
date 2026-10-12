def find_ticket(tickets, ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket

    return None

# tickets assignment
def assign_ticket(tickets, ticket_id, staff_name):
    ticket = find_ticket(tickets, ticket_id)

    if ticket is None:
        raise ValueError("Ticket not found.")

    if ticket["status"] == "resolved":
        raise ValueError("Reopen the ticket before modifying it.")

    staff_name = staff_name.strip()

    if not staff_name:
        raise ValueError("Staff name cannot be empty.")

    ticket["assigned_to"] = staff_name

    return ticket

# ticket update status
def update_status(tickets, ticket_id, new_status):
    ticket = find_ticket(tickets, ticket_id)

    if ticket is None:
        raise ValueError("Ticket not found.")

    new_status = new_status.strip().lower()
    current_status = ticket["status"]

    if current_status == "resolved":
        raise ValueError("Reopen the ticket before modifying it.")

    if new_status not in ["open", "in_progress", "resolved"]:
        raise ValueError("Invalid status.")

    if current_status == "open" and new_status == "in_progress":
        if not ticket["assigned_to"]:
            raise ValueError("Assign the ticket before starting work.")

    elif current_status == "in_progress" and new_status == "resolved":
        pass

    else:
        raise ValueError(
            f"Cannot change status from {current_status} to {new_status}."
        )

    ticket["status"] = new_status

    return ticket

# reopen a resolved ticket
def reopen_ticket(tickets, ticket_id):
    ticket = find_ticket(tickets, ticket_id)

    if ticket is None:
        raise ValueError("Ticket not found.")

    if ticket["status"] != "resolved":
        raise ValueError("Only resolved tickets can be reopened.")

    ticket["status"] = "open"

    return ticket