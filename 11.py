from functools import cache

with open('11.txt', 'r') as f:
	data = [l.split() for l in f.readlines()]
	data = {l[0][:-1]: set(l[1:]) for l in data}

@cache
def traverse_paths(part_num, src, dst, fft=False, dac=False):
	fft = fft or src == 'fft'
	dac = dac or src == 'dac'
	if src == dst:
		return 1 if part_num == 1 else int(fft and dac)
	return sum(traverse_paths(part_num, opt, dst, fft, dac) for opt in data[src])

print("Part 1:", traverse_paths(1, 'you', 'out'))
print("Part 2:", traverse_paths(2, 'svr', 'out'))
