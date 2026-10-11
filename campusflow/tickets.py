def calculate_priority(urgency, affected_users):
    if urgency == "high" and affected_users >= 10:
        return "critical"

    if urgency == "high" or affected_users >= 10:
        return "high"

    if urgency == "medium" or affected_users >= 3:
        return "medium"

    return "low"

def create_ticket(title, category, urgency, affected_users, tickets):
    title = title.strip()
    category = category.strip().title()
    urgency = urgency.strip().lower()

    if not title:
        raise ValueError("Title cannot be empty.")

    if category not in ["Network", "Hardware", "Software", "Other"]:
        raise ValueError("Invalid category.")

    if urgency not in ["low", "medium", "high"]:
        raise ValueError("Invalid urgency.")

    if isinstance(affected_users, bool) or not isinstance(affected_users, int):
        raise ValueError("Affected users must be a whole number.")

    if affected_users <= 0:
        raise ValueError("Affected users must be greater than zero.")

    used_numbers = [
        int(ticket["id"][1:])
        for ticket in tickets
        if ticket["id"].startswith("T") and ticket["id"][1:].isdigit()
    ]

    next_number = max(used_numbers, default=0) + 1
    ticket_id = f"T{next_number:03d}"

    ticket = {
        "id": ticket_id,
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": calculate_priority(urgency, affected_users),
        "status": "open",
        "assigned_to": None
    }

    tickets.append(ticket)
    return ticket