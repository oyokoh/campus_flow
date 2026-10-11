import unittest

from campusflow.tickets import calculate_priority, create_ticket


class TestTickets(unittest.TestCase):

    def test_critical_priority(self):
        self.assertEqual(calculate_priority("high", 12), "critical")

    def test_high_priority(self):
        self.assertEqual(calculate_priority("high", 2), "high")

    def test_medium_priority(self):
        self.assertEqual(calculate_priority("low", 4), "medium")

    def test_low_priority(self):
        self.assertEqual(calculate_priority("low", 1), "low")

    def test_blank_title_is_rejected(self):
        with self.assertRaises(ValueError):
            create_ticket("   ", "Network", "high", 12, [])

    def test_zero_users_are_rejected(self):
        with self.assertRaises(ValueError):
            create_ticket("Wi-Fi issue", "Network", "high", 0, [])

    def test_ticket_gets_an_id(self):
        tickets = []
        ticket = create_ticket("Wi-Fi issue", "network", "high", 12, tickets)

        self.assertEqual(ticket["id"], "T001")
        self.assertEqual(ticket["category"], "Network")
        self.assertEqual(ticket["priority"], "critical")

    def test_ticket_ids_are_unique(self):
        tickets = []

        first = create_ticket("Wi-Fi issue", "Network", "high", 12, tickets)
        second = create_ticket("Broken laptop", "Hardware", "low", 1, tickets)

        self.assertNotEqual(first["id"], second["id"])


if __name__ == "__main__":
    unittest.main()