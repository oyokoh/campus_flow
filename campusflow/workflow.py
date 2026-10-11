from campusflow.errors import TicketError

def find_ticket(tickets, ticket_id):
    """Return the ticket dict with this ID, or raise TicketError."""
    ticket_id = str(ticket_id).strip() .upper()
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    raise TicketError(f"unknown ticket ID '{ticket_id}'.")

def assign_ticket(tickets, ticket_id, staff_name):
    """Assign a ticket to a staff member and return the upadated ticket."""
    ticket = find_ticket(tickets, ticket_id)             # raises if the ID is unknown

    name = str(staff_name).strip()
    if not name:
        raise TicketError("staff name cannot be blank.")
    if ticket["status"] == "resolved":
        raise TicketError("Reopen the ticket before changing it.") 

    ticket["assigned_to"] = name              # the only change, done last
    return ticket      