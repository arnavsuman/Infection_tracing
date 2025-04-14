#TEST CASES

from solution import trace_infection, parse_interaction_log

def check_items_in_set(required_items, actual_set):
    # Check if all items in required_items are in actual_set
    if required_items.issubset(actual_set):  # issubset checks if all required items exist in the actual set
        return True
    else:
        return False

#---------------------------------------------------------------------------------------------------
print("TEST CASE 1: Basic Infection Spread")
log_data = [('P1', 'P2', 10), ('P2', 'P3', 20), ('P3', 'P4', 30)]
initial_infected = {'P1'}
contagious_period = 48
interaction_dict = parse_interaction_log(log_data)
infected_individuals = trace_infection(initial_infected, interaction_dict, contagious_period)
actual_output = {'P1', 'P2', 'P3', 'P4'}
if check_items_in_set(infected_individuals, actual_output):
    print("TEST CASE1: PASSED")
else:
    print("TEST CASE1: FAILED")
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
print("TEST CASE 2: No Spread Due to Time Constraint")
log_data = [('P1', 'P2', 10), ('P2', 'P3', 100)]
initial_infected = {'P1'}
contagious_period = 48
interaction_dict = parse_interaction_log(log_data)
infected_individuals = trace_infection(initial_infected, interaction_dict, contagious_period)
actual_output = {'P1', 'P2'}
if check_items_in_set(infected_individuals, actual_output):
    print("TEST CASE2: PASSED")
else:
    print("TEST CASE2: FAILED")
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
print("TEST CASE 3: Multiple Initial Infected Individuals")
log_data = [('P1', 'P2', 10), ('P3', 'P4', 20), ('P2', 'P3', 30)]
initial_infected = {'P1', 'P3'}
contagious_period = 48
interaction_dict = parse_interaction_log(log_data)
infected_individuals = trace_infection(initial_infected, interaction_dict, contagious_period)
actual_output = {'P1', 'P2', 'P3', 'P4'}
if check_items_in_set(infected_individuals, actual_output):
    print("TEST CASE3: PASSED")
else:
    print("TEST CASE3: FAILED")
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
print("TEST CASE  4: Circular Infection Spread")
log_data = [('P1', 'P2', 5), ('P2', 'P3', 15), ('P3', 'P1', 25)]
initial_infected = {'P1'}
contagious_period = 48
interaction_dict = parse_interaction_log(log_data)
infected_individuals = trace_infection(initial_infected, interaction_dict, contagious_period)
actual_output = {'P1', 'P2', 'P3'}
if check_items_in_set(infected_individuals, actual_output):
    print("TEST CASE4: PASSED")
else:
    print("TEST CASE4: FAILED")
#---------------------------------------------------------------------------------------------------