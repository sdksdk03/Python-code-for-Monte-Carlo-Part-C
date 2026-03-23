import numpy as np
import matplotlib.pyplot as plt

SIM_TIME = 180  # 3 hours


# Function to run a single simulation

def run_simulation(sim_time=SIM_TIME):
    arrival_times = []
    service_times = []
    waiting_times = []
    departure_times = []

    cashier1 = 0
    cashier2 = 0
    current_time = 0

    while current_time < sim_time:
        # Exponential interarrival (lambda = 1)
        interarrival = np.random.exponential(1)
        current_time += interarrival

        if current_time > sim_time:
            break

        arrival = current_time
        # Uniform service time (2-6 min)
        service = np.random.uniform(2, 6)

        # Assign to earliest available cashier
        if cashier1 <= cashier2:
            start = max(arrival, cashier1)
            cashier1 = start + service
        else:
            start = max(arrival, cashier2)
            cashier2 = start + service

        wait = start - arrival
        depart = start + service

        # Store data
        arrival_times.append(arrival)
        service_times.append(service)
        waiting_times.append(wait)
        departure_times.append(depart)

    # Compute metrics for this run
    avg_wait = np.mean(waiting_times)
    max_wait = np.max(waiting_times)
    prob_wait_5 = np.mean(np.array(waiting_times) > 5)
    utilisation = sum(service_times) / (2 * sim_time)  # 2 cashiers

    return avg_wait, max_wait, prob_wait_5, utilisation, waiting_times


# Part C: Single Simulation

avg_wait, max_wait, prob_wait_5, utilisation, waiting_times = run_simulation()

print("=== Single Simulation Results ===")
print(f"Average waiting time: {avg_wait:.2f} min")
print(f"Maximum waiting time: {max_wait:.2f} min")
print(f"Probability wait > 5 min: {prob_wait_5:.2f}")
print(f"Cashier utilization: {utilisation:.2f}")

# Histogram of waiting times
plt.figure()
plt.hist(waiting_times, bins=10, edgecolor='black')
plt.xlabel("Waiting Time (min)")
plt.ylabel("Number of Customers")
plt.title("Histogram of Waiting Times (Single Simulation)")
plt.show()

# Part D: Repeat Simulation 50 times

avg_waits = []

for _ in range(50):
    avg_wait, _, _, _, _ = run_simulation()
    avg_waits.append(avg_wait)

mean_wait = np.mean(avg_waits)
std_wait = np.std(avg_waits)

print("\n=== Results After 50 Simulations ===")
print(f"Mean of average waiting times: {mean_wait:.2f} min")
print(f"Standard deviation: {std_wait:.2f} min")

# Histogram of average waiting times across 50 simulations
plt.figure()
plt.hist(avg_waits, bins=10, edgecolor='black')
plt.xlabel("Average Waiting Time (min)")
plt.ylabel("Frequency")
plt.title("Distribution of Average Waiting Time (50 simulations)")
plt.show()

