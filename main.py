from campusflow.tickets import create_ticket
from campusflow.workflow import assign_ticket, update_status, reopen_ticket
from campusflow.reports import get_work_queue, get_report
from campusflow.storage import load_tickets, save_tickets


def show_menu():
    print("\nCampusFlow — Helpdesk Ticket Manager")
    print("1. Create a ticket")
    print("2. List all tickets")
    print("3. View a ticket by ID")
    print("4. Assign staff")
    print("5. Update ticket status")
    print("6. Reopen a resolved ticket")
    print("7. Show work queue")
    print("8. Show reports")
    print("9. Exit")

def list_tickets(tickets):
    if not tickets:
        print("No tickets found.")
        return

    for ticket in tickets:
        print("-" * 40)
        print(f"ID: {ticket['id']}")
        print(f"Title: {ticket['title']}")
        print(f"Category: {ticket['category']}")
        print(f"Urgency: {ticket['urgency']}")
        print(f"Affected users: {ticket['affected_users']}")
        print(f"Priority: {ticket['priority']}")
        print(f"Status: {ticket['status']}")
        print(f"Assigned to: {ticket['assigned_to']}")

    print("-" * 40)

def view_ticket(tickets, ticket_id):
    ticket_id = ticket_id.strip().upper()

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            print("-" * 40)
            print(f"ID: {ticket['id']}")
            print(f"Title: {ticket['title']}")
            print(f"Category: {ticket['category']}")
            print(f"Urgency: {ticket['urgency']}")
            print(f"Affected users: {ticket['affected_users']}")
            print(f"Priority: {ticket['priority']}")
            print(f"Status: {ticket['status']}")
            print(f"Assigned to: {ticket['assigned_to']}")
            print("-" * 40)
            return

    print("Ticket not found.")

def main():
    try:
        tickets = load_tickets()
    except ValueError as error:
        print(f"Error loading tickets: {error}")
        return

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter ticket title: ")
            category = input("Enter category (Network, Hardware, Software, Other): ")
            urgency = input("Enter urgency (low, medium, high): ")

            try:
                affected_users = int(input("Enter number of affected users: "))

                ticket = create_ticket(
                    title,
                    category,
                    urgency,
                    affected_users,
                    tickets,
                )

                save_tickets(tickets)
                print(f"Ticket {ticket['id']} created successfully.")

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            list_tickets(tickets)

        elif choice == "3":
            ticket_id = input("Enter ticket ID: ")
            view_ticket(tickets, ticket_id)

        elif choice == "4":
            ticket_id = input("Enter ticket ID: ").strip().upper()
            staff_name = input("Enter staff name: ")

            try:
                ticket = assign_ticket(tickets, ticket_id, staff_name)
                save_tickets(tickets)
                print(f"Ticket {ticket['id']} assigned to {ticket['assigned_to']} successfully.")
            except ValueError as error:
                print(f"Error: {error}")
        
        elif choice == "5":
            ticket_id = input("Enter ticket ID: ").strip().upper()
            print("Available statuses: in_progress, resolved")
            new_status = input("Enter new status: ").strip().lower()

            try:
                ticket = update_status(tickets, ticket_id, new_status)
                save_tickets(tickets)
                print(
                    f"Ticket {ticket['id']} status updated to "
                    f"{ticket['status']} successfully."
                )
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "6":
            ticket_id = input("Enter ticket ID to reopen: ").strip().upper()

            try:
                ticket = reopen_ticket(tickets, ticket_id)
                save_tickets(tickets)
                print(f"Ticket {ticket['id']} reopened successfully.")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "7":
            queue = get_work_queue(tickets)

            if not queue:
                print("No unresolved tickets in the work queue.")
            else:
                print("\nCampusFlow Work Queue")
                print("-" * 40)

                for ticket in queue:
                    print(
                        f"{ticket['id']} | "
                        f"{ticket['priority'].upper()} | "
                        f"{ticket['status']} | "
                        f"{ticket['title']}"
                    )

        elif choice == "8":
            report = get_report(tickets)

            print("\nCampusFlow Ticket Report")
            print("-" * 35)
            print(f"Total tickets: {report['total']}")

            print("\nTickets by status:")
            for status, count in report["by_status"].items():
                print(f"{status}: {count}")

            print("\nTickets by priority:")
            for priority, count in report["by_priority"].items():
                print(f"{priority}: {count}")

            print("-" * 35)

        elif choice == "9":
            save_tickets(tickets)
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()