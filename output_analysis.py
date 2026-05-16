import random
import statistics


waiting_times = []

for i in range(50):
    wait = random.randint(1, 10)
    waiting_times.append(wait)


welch_average = statistics.mean(waiting_times)


replications = []
for i in range(5):
    sample = [random.randint(1, 10) for x in range(10)]
    sample.pop(0)  # delete warm-up
    replications.append(statistics.mean(sample))

replication_average = statistics.mean(replications)


batch_size = 10
batches = []

for i in range(0, len(waiting_times), batch_size):
    batch = waiting_times[i:i+batch_size]
    batches.append(statistics.mean(batch))

batch_average = statistics.mean(batches)


print("=== OUTPUT ANALYSIS RESULTS ===")
print("Welch Method Average:", welch_average)
print("Replication Deletion Average:", replication_average)
print("Batch Mean Average:", batch_average)
