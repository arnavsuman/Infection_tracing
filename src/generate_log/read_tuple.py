def read_logs_from_file(filename="meeting_logs.txt"):
    logs = set()
    
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(", ")  # Split by comma and space
            if len(parts) == 3:  # Ensure valid format
                p1, p2, time = parts[0], parts[1], int(parts[2])
                logs.add((p1, p2, time))  # Store as a tuple
    
    return logs

# Example usage
logs_from_file = read_logs_from_file()
#print(logs_from_file)
