# CampusFlow Design Decisions

## 1. Project Structure

We separated the project into modules so that each file has a specific responsibility.

- `tickets.py` handles ticket creation and priority calculation.
- `workflow.py` handles ticket assignment and status changes.
- `reports.py` generates the work queue and ticket reports.
- `storage.py` saves and loads tickets using JSON.
- `main.py` provides the command-line menu and connects the modules.

This structure makes the code easier to understand, test, and maintain.

## 2. Ticket Data Structure

We used Python dictionaries to represent tickets because each ticket contains named fields such as its ID, title, category, urgency, priority, status, and assigned staff member.

We stored the tickets in a list so that the application can manage multiple tickets.

## 3. Priority Calculation

We created a separate function to calculate ticket priority based on urgency and the number of affected users.

This keeps the priority rules in one place and makes them easier to test.

## 4. Ticket Identification

Each ticket receives a unique ID in the format `T001`, `T002`, and so on.

The next ID is calculated using the highest existing numeric ticket ID. This helps prevent duplicate IDs when tickets are loaded from saved data.

## 5. Workflow Rules

We separated ticket assignment and status changes into workflow functions.

A ticket must be assigned before it can move into progress. A resolved ticket must be reopened before it can be modified through the normal workflow.

These rules help prevent invalid ticket transitions.

## 6. JSON Persistence

We used JSON to save tickets between application runs.

The application starts with an empty ticket list if the data file does not exist. If the JSON file is malformed, the application reports an error instead of silently treating the saved data as empty.

## 7. Automated Testing

We used Python's `unittest` framework to test ticket creation, validation, workflow rules, reporting, queue ordering, and data storage.

Automated tests help me check that the application behaves as expected when I make changes.