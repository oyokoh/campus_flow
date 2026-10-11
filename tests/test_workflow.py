import unittest

from campusflow.errors import TicketError
from campusflow.workflow import assign_ticket, find_ticket


def make_ticket(ticket_id="T001", status="open", priority="low", assigned_to=None):
    """Small helper so each test can build a ticket quickly."""
    return {
        "id": ticket_id,
        "title": "Test ticket",
        "category": "Other",
        "urgency": "low",
        "affected_users": 1,
        "priority": priority,
        "status": status,
        "assigned_to": assigned_to,
    }


class TestAssign(unittest.TestCase):
    def test_assign_sets_staff_name(self):
        tickets = [make_ticket()]
        result = assign_ticket(tickets, "T001", "  Ada  ")
        self.assertEqual(result["assigned_to"], "Ada")

    def test_unknown_ticket_is_rejected(self):
        tickets = [make_ticket()]
        with self.assertRaises(TicketError):
            assign_ticket(tickets, "T999", "Ada")

    def test_blank_name_is_rejected_and_ticket_unchanged(self):
        tickets = [make_ticket()]
        with self.assertRaises(TicketError):
            assign_ticket(tickets, "T001", "   ")
        self.assertIsNone(tickets[0]["assigned_to"])

    def test_resolved_ticket_cannot_be_assigned(self):
        tickets = [make_ticket(status="resolved", assigned_to="Ada")]
        with self.assertRaises(TicketError):
            assign_ticket(tickets, "T001", "John")
        self.assertEqual(tickets[0]["assigned_to"], "Ada")


if __name__ == "__main__":
    unittest.main()