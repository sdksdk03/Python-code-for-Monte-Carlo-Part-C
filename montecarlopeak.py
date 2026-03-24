import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
SIM_TIME = 180
# 1 SIMULATION
def run_simulation(sim_time=SIM_TIME):
    service_times = []
    waiting_times = []

    cashier1 = 0
    cashier2 = 0
    current_time = 0

    while current_time < sim_time:
        interarrival = np.random.exponential(1)
        current_time += interarrival

        if current_time > sim_time:
            break

        arrival = current_time
        service = np.random.uniform(2, 6)

        if cashier1 <= cashier2:
            start = max(arrival, cashier1)
            cashier1 = start + service
        else:
            start = max(arrival, cashier2)
            cashier2 = start + service

        wait = start - arrival

        service_times.append(service)
        waiting_times.append(wait)

    avg_wait = np.mean(waiting_times)
    max_wait = np.max(waiting_times)
    prob_wait_5 = np.mean(np.array(waiting_times) > 5)
    utilisation = sum(service_times) / (2 * sim_time)

    return avg_wait, max_wait, prob_wait_5, utilisation, waiting_times
# SIMULATION FUNCTION

def run_peak_simulation(sim_time=SIM_TIME):
    service_times = []
    waiting_times = []

    cashier1 = 0
    cashier2 = 0
    current_time = 0

    while current_time < sim_time:
        # Peak in last 60 minutes
        if current_time < 120:
            interarrival = np.random.exponential(1)
        else:
            interarrival = np.random.exponential(0.5)

        current_time += interarrival

        if current_time > sim_time:
            break

        arrival = current_time
        service = np.random.uniform(2, 6)

        if cashier1 <= cashier2:
            start = max(arrival, cashier1)
            cashier1 = start + service
        else:
            start = max(arrival, cashier2)
            cashier2 = start + service

        wait = start - arrival

        service_times.append(service)
        waiting_times.append(wait)

    avg_wait = np.mean(waiting_times)
    max_wait = np.max(waiting_times)
    prob_wait_5 = np.mean(np.array(waiting_times) > 5)
    utilisation = sum(service_times) / (2 * sim_time)

    return avg_wait, max_wait, prob_wait_5, utilisation, waiting_times

# PART C – SINGLE SIMULATION
avg_wait, max_wait, prob_wait_5, utilisation, waiting_times = run_simulation()
table_C = pd.DataFrame({
    "Metric": ["Average Waiting Time", "Maximum Waiting Time", "P(wait > 5 min)", "Utilisation"],
    "Value": [avg_wait, max_wait, prob_wait_5, utilisation]
})

print("\n=== Part C: Single Simulation Results ===")
print(table_C)

# Histogram
plt.figure()
plt.hist(waiting_times, bins=10)
plt.title("Waiting Times (Single Simulation)")
plt.xlabel("Waiting Time")
plt.ylabel("Frequency")
plt.show()
# PART D – 50 SIMULATIONS

avg_waits = []

for _ in range(50):
    avg, _, _, _, _ = run_simulation()
    avg_waits.append(avg)

mean_wait = np.mean(avg_waits)
std_wait = np.std(avg_waits)

table_D = pd.DataFrame({
    "Metric": ["Mean Waiting Time (50 runs)", "Standard Deviation"],
    "Value": [mean_wait, std_wait]
})

print("\n=== Part D: Repetition Results ===")
print(table_D)

# Histogram
plt.figure()
plt.hist(avg_waits, bins=10)
plt.title("Average Waiting Times (50 Simulations)")
plt.xlabel("Average Waiting Time")
plt.ylabel("Frequency")
plt.show()
#  PART F – PEAK VS NORMAL TABLE

avg_n, max_n, prob_n, util_n, _ = run_simulation()
avg_p, max_p, prob_p, util_p, waiting_peak = run_peak_simulation()

table_F = pd.DataFrame({
    "Metric": ["Average Waiting Time", "Maximum Waiting Time", "P(wait > 5 min)", "Utilisation"],
    "Normal": [avg_n, max_n, prob_n, util_n],
    "Peak": [avg_p, max_p, prob_p, util_p]
})

print("\n=== Part F: Normal vs Peak Comparison ===")
print(table_F)

# Histogram for peak
plt.figure()
plt.hist(waiting_peak, bins=10)
plt.title("Waiting Times (Peak Hour)")
plt.xlabel("Waiting Time")
plt.ylabel("Frequency")
plt.show()