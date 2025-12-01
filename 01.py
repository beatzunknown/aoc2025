with open('01.txt', 'r') as f:
    data = [(-1 if l[0] == 'L' else 1, int(l.rstrip()[1:])) for l in f.readlines()]

pos = 50
part_1 = part_2 = 0

for direction, rots in data:
	old_pos = pos
	pos = (pos + direction * rots) % 100
	part_1 += (pos == 0)

	gap_to_zero = old_pos if direction == -1 else (100 - old_pos)
	if old_pos != 0 and rots >= gap_to_zero:
		part_2 += 1
		rots -= gap_to_zero

	part_2 += (rots // 100)

print("Part 1:", part_1)
print("Part 2:", part_2)
