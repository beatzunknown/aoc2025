import math
from collections import defaultdict
from functools import lru_cache, reduce
from itertools import combinations, groupby
from z3 import Int, Optimize

with open('xx.txt', 'r') as f:
	data = [l.rstrip() for l in f.readlines()]
	nums = [list(map(int, l.rstrip())) for l in f.readlines()]
	ranges = [tuple(map(int, l.rstrip().split('-'))) for l in f.readlines()]
	coords = [tuple(map(int, l.rstrip().split(','))) for l in f.readlines()]
	grid = [[c for c in l.rstrip()] for l in f.readlines()]

part_1 = 0
part_2 = 0

print("Part 1:", part_1)
print("Part 2:", part_2)
