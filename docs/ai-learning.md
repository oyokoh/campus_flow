# CampusFlow AI Learning Log

## 1. Purpose

We used AI as a learning assistant while developing CampusFlow, a command-line ticket management application written in Python.

Our goal was to understand the code and the reasons behind the design decisions, rather than simply copy solutions.

## 2. Areas Where I Used AI

We used AI to help us understand and work through the following areas:

- **Project structure:** Understanding how to divide the application into modules.
- **Ticket management:** Learning how to create tickets, validate input, and calculate priority.
- **Workflow:** Understanding ticket assignment and valid status transitions.
- **Data persistence:** Learning how to save and load ticket data using JSON.
- **Reporting:** Understanding how to count tickets and sort the work queue.
- **Testing:** Learning how to run automated tests and interpret test results.
- **Documentation:** Organizing the README and documenting design decisions.

## 3. What I Learned

During development, I learned that separating code into modules makes a project easier to maintain and test.

We also learned how to use Python dictionaries and lists to represent and manage ticket data, how to handle invalid input with exceptions, and how to use JSON for persistence.

Writing and running automated tests helped me check whether individual parts of the application behaved as expected.

## 4. How I Verified the Work

We ran the automated test suite using:

`python -m unittest discover -s tests -v`

The test run reported 26 passing tests.

This helped me verify the implemented ticket, workflow, reporting, and storage behavior covered by those tests.

## 5. Reflection

Using AI was most useful when I asked for explanations of errors, worked through problems step by step, and checked my understanding of the code.

We still need to be able to explain the main functions, the ticket priority rules, the workflow restrictions, and how the application saves and loads data.

Our goal is to keep improving my Python skills and become more confident solving programming problems independently.