# CampusFlow — Campus Helpdesk Ticket Manager

## Overview

CampusFlow is a Python command-line application for managing campus IT support tickets. It helps users record technical issues, calculate priorities, assign staff, track progress, and generate reports.

## Features

- Create tickets with unique IDs.
- Categorize issues as Network, Hardware, Software, or Other.
- Calculate ticket priority based on urgency and affected users.
- List all tickets or view a ticket by ID.
- Assign staff to tickets.
- Track ticket status from open to in progress and resolved.
- Reopen resolved tickets.
- Display a work queue sorted by priority.
- Generate ticket reports by status and priority.
- Save and load tickets using JSON persistence.

## Requirements

- Python 3.12 or compatible Python 3 version.
- No third-party packages are required for the current implementation.

## How to Run

Clone or download the project, then navigate to its root directory.

Run the application:

```bash
python3 main.py
```

Follow the numbered menu options to manage tickets.

## Running Tests

Run the automated test suite:

```bash
python3 -m unittest discover -s tests -v
```

## Data Storage

Ticket data is stored in `data/tickets.json`. If the file does not exist, the application starts with an empty ticket list. Invalid JSON data produces an error rather than silently resetting the data.

## Ticket Workflow

Tickets follow this workflow:

`open` → `in_progress` → `resolved`

A ticket must be assigned before work can begin. Resolved tickets must be reopened before they can be modified.

## Project Structure

- `main.py` — command-line menu and application entry point.
- `campusflow/tickets.py` — ticket creation and priority calculation.
- `campusflow/workflow.py` — assignment and status transitions.
- `campusflow/reports.py` — work queue and reports.
- `campusflow/storage.py` — JSON persistence.
- `tests/` — automated unit tests.
- `docs/` — project design decisions and AI learning log.
