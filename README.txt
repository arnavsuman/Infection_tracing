Contact Tracing Analysis

Solution Overview

This program implements an infection tracing system based on interaction logs. It takes a list of interactions between 
individuals at specific time points and traces the spread of an infection from an initial infected individual. 
The system uses a breadth-first search (BFS) approach to determine individuals who were in contact with the infected 
person within a given contagious period.

Key Features:

-> Parses interaction logs where each entry consists of (person1, person2, time).

-> Finds all contacts of a given person within a defined contagious period.

-> Traces the infection spread iteratively using BFS.

-> Outputs the list of potentially infected individuals.

CODE EXPLANATION

1. Generating Random Meeting Logs
    The function generate_logs(num_meetings) creates a set of random meetings.

    There are 10 individuals (P1 to P10).

    Each meeting is a tuple containing two people and a random meeting time (0 to 72 hours).

    To ensure unique meetings, a set is used.

    The generated logs are written to a file (meeting_logs.txt) in comma-separated format.


2.Reading Log Files
    This function reads the previously saved meeting logs.

    Each line is split into three parts: person1, person2, and meeting time.

    The logs are stored as a set of tuples to avoid duplicates.

    The function ensures data integrity by checking that each line has exactly three parts.


3.Parsing Logs into a Dictionary
    The function converts the set of tuples into a dictionary where:

    Keys → Time of interaction.

    Values → List of tuples (pairs of people who met at that time).

    This helps in quick lookups when checking for contacts at a specific time.


4.Finding Contacts of an Infected Person
    Given a person and a time, this function finds all people they met within the contagious period.

    The function iterates over a time window (time to time + contagious_period).

    It checks if the person appears in any meeting log and stores the other person as a contact.

    This simulates the potential spread of infection.


5. Tracing the Infection Spread
    Simulates the spread of infection from an initially infected individual.

    Uses a queue-based approach (BFS-like algorithm) to track spread.

    For each infected person:

    Their contacts are found within the contagious period.

    If a contact is not already infected, they are added to the infected list.

    The process continues until there are no new infections.

    This method ensures all infected individuals are traced.


Limitations
1. Assumes every meeting has an equal infection risk.

2. The program assumes that interactions are limited to a maximum of 10 individuals meeting within a 72-hour window.

3. It does not account for varying infection probabilities (e.g., different transmission risks based on interaction duration or proximity).

4. Assumes infection is transmitted instantly upon meeting.

5. The program assumes interactions are provided in a structured format and do not contain missing or incorrect values.

6. It operates under the assumption that once a person is infected, they remain contagious for the full duration of the contagious_period ie, Does not account for recovery or immunity.


How to Compile and Run

Prerequisites
Ensure you have Python installed on your system (Python 3.6 or later is recommended).

Steps to Run the Program

    1. Clone or download the project files.

    2. Ensure that the generate_log.read_tuple module is available and correctly imports interaction logs.

    3. Run module generate_logs.py first to generate meeting_logs.

    4. Open a terminal or command prompt and navigate to the directory containing the script.

    5. Run the script using the following command: python solution.py

HOW TO EXECUTE TEST CASES
Run the test script (test_cases.py) using the command:
    python test_cases.py

Interpreting the Results

If a test case passes, you will see: TEST CASE X: PASSED
If a test case fails, you will see: TEST CASE X: FAILED

If all test cases pass you should see:
    TEST CASE 1: Basic Infection Spread
    TEST CASE1: PASSED
    TEST CASE 2: No Spread Due to Time Constraint
    TEST CASE2: PASSED
    TEST CASE 3: Multiple Initial Infected Individuals
    TEST CASE3: PASSED
    TEST CASE  4: Circular Infection Spread
    TEST CASE4: PASSED