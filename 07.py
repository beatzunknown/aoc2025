from functools import lru_cache

with open('07.txt', 'r') as f:
	grid = [l.rstrip() for l in f.readlines()]

# part 1: count number of times beam hits splitter
def forward_beam(r, c, visited=set()):
	if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
		return 0
	if (r, c) in visited:
		return 0
	visited.add((r, c))
	if grid[r][c] == '^':
		return 1 + forward_beam(r+1, c-1, visited) + forward_beam(r+1, c+1, visited)
	return forward_beam(r+1, c, visited)

# part 2: count number of distinct paths beam takes through splitters
@lru_cache
def track_beam_paths(r, c):
	if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
		return 0
	for r in range(r, len(grid)):
		if grid[r][c] == '^':
			return track_beam_paths(r, c-1) + track_beam_paths(r, c+1)
	return 1

print("Part 1:", forward_beam(1, grid[0].index('S')))
print("Part 2:", track_beam_paths(1, grid[0].index('S')))
