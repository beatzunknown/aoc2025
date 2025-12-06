import math
from itertools import groupby

with open('06.txt', 'r') as f:
	data_orig = [l.rstrip('\n') for l in f.readlines()]

cw_rot = lambda matrix: list(map(list, zip(*reversed(matrix))))
ccw_rot = lambda matrix: list(map(list, zip(*matrix)))[::-1]
ops = {'*': math.prod, '+': sum}

problems = ccw_rot([l.split() for l in data_orig])

part_1 = 0
for problem in problems:
	operator = problem[-1]
	nums = [int(num) for num in problem[:-1]]
	part_1 += ops[operator](nums)

# for part 2: rotate CCW, group by problems, then solve each row (was column before rotate)
rotated_data = ccw_rot(data_orig)
# grouping is by row that is all empty space
grouped_data = groupby(rotated_data, key=lambda group: all(not x.strip() for x in group))
problems = [list(g) for k, g in grouped_data if not k]

part_2 = 0
for problem in problems:
	operator = problem[-1][-1]
	nums = [int(''.join(x[:-1]).strip()) for x in problem]
	part_2 += ops[operator](nums)

print("Part 1:", part_1)
print("Part 2:", part_2)
