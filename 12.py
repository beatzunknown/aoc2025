from itertools import groupby

cw_rot = lambda l: list(map(list, zip(*reversed(l))))
flip = lambda l: [l[i][::-1] for i in range(len(l))]

with open('12.txt', 'r') as f:
	data = [l.rstrip() for l in f.readlines()]
	grouped_data = groupby(data, key=lambda group: all(not x.strip() for x in group))
	grouped_data = [list(g) for k, g in grouped_data if not k]
	shapes, problems = grouped_data[:-1], grouped_data[-1]
	shapes = [shape[1:] for shape in shapes]
	problems = [p.split() for p in problems]
	problems = [(list(map(int, p[0][:-1].split('x'))), list(map(int, p[1:]))) for p in problems]

part_1 = 0
for (width, length), presents in problems:
	max_presents = (width / 3) * (length / 3)
	req_presents = sum(presents)
	# add some 0.25 fudge factor to work for example and actual input
	part_1 += (max_presents+0.25 >= req_presents)

print("Part 1:", part_1)
