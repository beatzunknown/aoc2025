from functools import reduce
from itertools import combinations
from z3 import Int, Optimize

with open('10.txt', 'r') as f:
	data = [l.rstrip().split(' ') for l in f.readlines()]

part_1 = 0
part_2 = 0

# converts list of toggles (eg: [0, 2] means items 0 and 2 are toggled)
# to vector (eg: [1, 0, 1, 0] for size 4 vector where only 0 and 2 indexes toggled)
def toggle_list_to_vec(toggles, n):
	vector = [0] * n
	for toggle in toggles:
		vector[toggle] = 1
	return vector

def get_num_button_presses(button_vecs, target_lights_vec):
	for n in range(1, len(button_vecs)*2):
		for options in combinations(button_vecs, n):
			# element-wise xor list of lists
			lights_vec = reduce(lambda x, y: [x[i] ^ y[i] for i in range(len(x))], list(options))
			if lights_vec == target_lights_vec:
				return n

for line in data:
	target_lights = line[0][1:-1]
	buttons = [list(map(int, x[1:-1].split(','))) for x in line[1:-1]]
	joltages = list(map(int, line[-1][1:-1].split(',')))

	num_pos = len(target_lights) # number of light/joltage positions
	num_btn = len(buttons) # number of buttons available
	lights_vec = [int(target_lights[i] == '#') for i in range(num_pos)]
	button_vecs = [toggle_list_to_vec(button, num_pos) for button in buttons]

	part_1 += get_num_button_presses(button_vecs, lights_vec)

	# variables to solve/optimize are the number of presses per button
	presses = [Int(f'presses_{i}') for i in range(num_btn)]
	equations = []
	for j in range(num_pos):
		# for each joltage position, solve equation of positional_button_toggle * num_presses
		equations.append(joltages[j] == sum([button_vecs[i][j]*presses[i] for i in range(num_btn)]))
	for i in range(num_btn):
		# enforce that negative number of button presses impossible
		equations.append(presses[i] >= 0)

	optimizer = Optimize()
	optimizer.add(equations)
	optimizer.minimize(sum(presses))
	optimizer.check()
	model = optimizer.model()
	part_2 += sum([model[x].as_long() for x in model])

print("Part 1:", part_1)
print("Part 2:", part_2)
