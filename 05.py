from itertools import groupby

with open('05.txt', 'r') as f:
	data = [l.rstrip() for l in f.readlines()]

# get input groups partitioned by blank lines
grouped_data = groupby(data, key=lambda x: x == '')
ranges, ingredients = [list(g) for k, g in grouped_data if not k]
ranges = sorted([list(map(int, r.split('-'))) for r in ranges])
ingredients = set(map(int, ingredients))

# remove all identified fresh ingredients from total set
bad_ingredients = ingredients.copy()
for start, end in ranges:
	for ingredient in ingredients:
		if start <= ingredient <= end:
			bad_ingredients.discard(ingredient)

# compact all ranges with overlap, since ranges are sorted
compacted_ranges = []
for start, end in ranges:
	has_modified_existing_range = False
	for i in range(len(compacted_ranges)):
		a, b = compacted_ranges[i]
		# if no range overlap, skip
		if start > b or a > end:
			continue
		compacted_ranges[i] = [min(a, start), max(b, end)]
		has_modified_existing_range = True
		break
	# if we did no compaction, we need to add new range
	if not has_modified_existing_range:
		compacted_ranges.append([start, end])

print("Part 1:", len(ingredients) - len(bad_ingredients))
print("Part 2:", sum(list(map(lambda x: x[1]-x[0]+1, compacted_ranges))))
