from collections import defaultdict

with open('02.txt', 'r') as f:
    ranges = [list(map(int, l.rstrip().split('-'))) for l in f.readline().split(',')]

sol = defaultdict(int)

for start, end in ranges:
	for num in range(start, end+1):
		num = str(num)
		n = len(num)
		for partitions in range(2, n+1):
			if n % partitions:
				continue
			size = n//partitions
			chunks = [num[i:i+size] for i in range(0, n, size)]
			if len(set(chunks)) == 1:
				sol[partitions] += int(num)
				break

print("Part 1:", sol[2])
print("Part 2:", sum(sol.values()))
