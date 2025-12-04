with open('04.txt', 'r') as f:
    grid = [[c for c in l.rstrip()] for l in f.readlines()]

n_rows = len(grid)
n_cols = len(grid[0])

def count_neighbours(grid, r, c):
    num = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            if r+dr < 0 or r+dr >= n_rows or c+dc < 0 or c+dc >= n_cols:
                continue
            if grid[r+dr][c+dc] == '@':
                num += 1
    return num

def access_paper(grid, should_remove_after_access):
    num_accessed = 0
    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] != '@':
                continue
            if count_neighbours(grid, r, c) < 4:
                num_accessed += 1
                if should_remove_after_access:
                    grid[r][c] = '.'
    return num_accessed

part_1 = access_paper(grid, should_remove_after_access=False)
part_2 = 0

while (removed := access_paper(grid, should_remove_after_access=True)):
    part_2 += removed

print("Part 1:", part_1)
print("Part 2:", part_2)
