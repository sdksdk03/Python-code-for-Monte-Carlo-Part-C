import numpy as np

SIM_TIME = 180

arrival_times = []
service_times = []
start_times = []
waiting_times = []
departure_times = []

# cashier availability
cashier1 = 0
cashier2 = 0

current_time = 0

while current_time < SIM_TIME:
    # generate interarrival time
    interarrival = np.random.exponential(1)
    current_time += interarrival
    
    if current_time > SIM_TIME:
        break

    arrival = current_time
    service = np.random.uniform(2, 6)

    # choose earliest cashier
    if cashier1 <= cashier2:
        start = max(arrival, cashier1)
        cashier1 = start + service
    else:
        start = max(arrival, cashier2)
        cashier2 = start + service

    wait = start - arrival
    depart = start + service

    # store
    arrival_times.append(arrival)
    service_times.append(service)
    start_times.append(start)
    waiting_times.append(wait)
    departure_times.append(depart)

# metrics
avg_wait = np.mean(waiting_times)
max_wait = np.max(waiting_times)
prob_wait_5 = np.mean(np.array(waiting_times) > 5)

utilisation = (sum(service_times)) / (2 * SIM_TIME)

print("Average wait:", avg_wait)
print("Max wait:", max_wait)
print("P(wait > 5):", prob_wait_5)
print("Utilisation:", utilisation)