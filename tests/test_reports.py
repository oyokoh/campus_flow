import unittest

from campusflow.reports import get_work_queue, get_report


def make_ticket(ticket_id, priority, status="open"):
    return {
        "id": ticket_id,
        "title": f"Issue {ticket_id}",
        "category": "Network",
        "urgency": "high",
        "affected_users": 10,
        "priority": priority,
        "status": status,
        "assigned_to": None,
    }


class TestReports(unittest.TestCase):

    def test_queue_sorts_by_priority(self):
        tickets = [
            make_ticket("T001", "low"),
            make_ticket("T002", "critical"),
            make_ticket("T003", "high"),
        ]

        queue = get_work_queue(tickets)

        self.assertEqual(
            [ticket["id"] for ticket in queue],
            ["T002", "T003", "T001"],
        )

    def test_queue_sorts_equal_priorities_by_id(self):
        tickets = [
            make_ticket("T010", "high"),
            make_ticket("T002", "high"),
            make_ticket("T001", "high"),
        ]

        queue = get_work_queue(tickets)

        self.assertEqual(
            [ticket["id"] for ticket in queue],
            ["T001", "T002", "T010"],
        )

    def test_resolved_tickets_are_excluded(self):
        tickets = [
            make_ticket("T001", "critical", "resolved"),
            make_ticket("T002", "low", "open"),
        ]

        queue = get_work_queue(tickets)

        self.assertEqual(
            [ticket["id"] for ticket in queue],
            ["T002"],
        )

    def test_report_counts_status_and_priority(self):
        tickets = [
            make_ticket("T001", "critical", "open"),
            make_ticket("T002", "high", "in_progress"),
            make_ticket("T003", "low", "resolved"),
        ]

        report = get_report(tickets)

        self.assertEqual(report["total"], 3)
        self.assertEqual(report["by_status"]["open"], 1)
        self.assertEqual(report["by_status"]["in_progress"], 1)
        self.assertEqual(report["by_status"]["resolved"], 1)
        self.assertEqual(report["by_priority"]["critical"], 1)
        self.assertEqual(report["by_priority"]["high"], 1)
        self.assertEqual(report["by_priority"]["medium"], 0)
        self.assertEqual(report["by_priority"]["low"], 1)

    def test_empty_report(self):
        report = get_report([])

        self.assertEqual(report["total"], 0)
        self.assertEqual(report["by_status"]["open"], 0)
        self.assertEqual(report["by_priority"]["critical"], 0)


if __name__ == "__main__":
    unittest.main()