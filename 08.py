import math
from collections import defaultdict

def euclid_dist(a, b):
	return math.sqrt(sum((a_i - b_i) ** 2 for a_i, b_i in zip(a, b)))

with open('08.txt', 'r') as f:
	data = [list(map(int, l.rstrip().split(','))) for l in f.readlines()]
	num_boxes = len(data)

dists = []
for i in range(num_boxes):
	for j in range(i+1, num_boxes):
		dist = euclid_dist(data[i], data[j])
		dists.append((dist, i, j))

# circuit lookup by junction box ID
circuits = {i: set([i]) for i in range(num_boxes)}
num_pairs = 0

for dist, i, j in sorted(dists):
	num_pairs += 1
	new_circuit = circuits[i] | circuits[j]
	for x in new_circuit:
		circuits[x] = new_circuit

	if len(new_circuit) == num_boxes:
		part_2 = data[i][0] * data[j][0]
		break
	elif num_pairs == 1000:
		distinct_circuits = set(map(frozenset, circuits.values()))
		circuit_sizes = sorted(list(map(len, distinct_circuits)), reverse=True)
		part_1 = math.prod(circuit_sizes[:3])

print("Part 1:", part_1)
print("Part 2:", part_2)
