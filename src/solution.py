from generate_log.read_tuple import read_logs_from_file
logs = read_logs_from_file()

from collections import defaultdict

def parse_interaction_log(log_data):
    # Parses the interaction log and stores it in a dictionary where keys are times
    # and values are sets of interacting individuals.

    interactions = defaultdict(list)
    
    for person1, person2, time in log_data:
        interactions[time].append((person1, person2))
    
    return interactions

def find_contacts(person, time, log_data, contagious_period):

    #Finds all people a given person contacted within the contagious period.

    contacts = set()
    for t in range(time, time + contagious_period + 1):  # Check within time window
        for p1, p2 in log_data.get(t, []):
            if person == p1:
                contacts.add(p2)
            elif person == p2:
                contacts.add(p1)
    return contacts

def trace_infection(initial_infected, log_data, contagious_period):

    #Traces the infection and returns a list of infected individuals.

    infected = set(initial_infected)
    queue = [(person, 0) for person in initial_infected]  # (person, infection_time)
    
    while queue:
        person, infection_time = queue.pop(0)
        for t in range(infection_time, infection_time + contagious_period + 1):
            contacts = find_contacts(person, t, log_data, contagious_period)
            for contact in contacts:
                if contact not in infected:
                    infected.add(contact)
                    queue.append((contact, t))
    
    return infected

def main():
    
    # List of  infected individuals
    initial_infected = ['P6']
    
    # Contagious period in hours
    contagious_period = 48
    
    # Parse log data
    interaction_dict = parse_interaction_log(logs)
    
    # Trace infection spread
    infected_individuals = trace_infection(initial_infected, interaction_dict, contagious_period)
    
    # Output result
    print("Potentially Infected Individuals:", infected_individuals)

if __name__ == "__main__":
    main()
