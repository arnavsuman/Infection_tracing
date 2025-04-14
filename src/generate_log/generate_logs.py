import random


def generate_meeting_logs(num_meetings=20):
    people = [f"P{i}" for i in range(1, 11)]  # P1 to P10
    logs = set()

    while len(logs) < num_meetings:
        p1, p2 = random.sample(people, 2)  # Select two different people
        meeting_time = random.randint(0, 72)  # Random time within 0 to 72 hours
        logs.add((p1, p2, meeting_time))  # Store unique meetings

    return logs

def save_logs_to_file(logs, filename="meeting_logs.txt"):
    with open(filename, "w") as file:
        for log in logs:
            file.write(f"{log[0]}, {log[1]}, {log[2]}\n")  # Write each log as CSV format

# Example usage
meeting_logs = generate_meeting_logs(5)
save_logs_to_file(meeting_logs)
print("Logs saved successfully!")
