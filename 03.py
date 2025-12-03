with open('03.txt', 'r') as f:
    data = [l.rstrip() for l in f.readlines()]

def solve(data, num_batteries):
	total_joltage = 0
	for bank in data:
		bank_joltage = ""
		for i in range(num_batteries-1, 0, -1):
			max_batt_joltage = max(bank[:-i])
			max_idx = bank.index(max_batt_joltage)
			bank_joltage += max_batt_joltage
			bank = bank[max_idx+1:]

		bank_joltage += max(bank)
		total_joltage += int(bank_joltage)
	return total_joltage

print("Part 1:", solve(data, 2))
print("Part 2:", solve(data, 12))
