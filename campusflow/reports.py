PRIORITY_ORDER = {
    "critical": 1,
    "high": 2,
    "medium": 3,
    "low": 4,
}


def get_work_queue(tickets):
    unresolved = [
        ticket for ticket in tickets
        if ticket["status"] != "resolved"
    ]

    return sorted(
        unresolved,
        key=lambda ticket: (
            PRIORITY_ORDER[ticket["priority"]],
            int(ticket["id"][1:])
        )
    )


def get_report(tickets):
    statuses = ["open", "in_progress", "resolved"]
    priorities = ["critical", "high", "medium", "low"]

    report = {
        "total": len(tickets),
        "by_status": {},
        "by_priority": {},
    }

    for status in statuses:
        report["by_status"][status] = sum(
            1 for ticket in tickets
            if ticket["status"] == status
        )

    for priority in priorities:
        report["by_priority"][priority] = sum(
            1 for ticket in tickets
            if ticket["priority"] == priority
        )

    return report