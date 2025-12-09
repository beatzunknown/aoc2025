from itertools import combinations

with open('09.txt', 'r') as f:
	# points are (x, y) tuples where top-left coord is (0, 0)
	points = [tuple(map(int, l.rstrip().split(','))) for l in f.readlines()]

'''
The trick for part 2 (is rectangle fully in polygon) is
realising you don’t need to validate if a rectangle corner
is in the red/green polygon (which I attempted first). You
only need to validate if any other lines have a non-border
overlap with the rectangle. If it does, you know there’s a
part of the rectangle that’s not green/red because there’s
“something else” inside it.
'''

def no_lines_overlap_with_rect(p1, p2):
	# rectangle corner coordinates, where (x1, y1) is upper left, and (x2, y2) bottom right
	rect_x1, rect_x2 = sorted([p1[0], p2[0]])
	rect_y1, rect_y2 = sorted([p1[1], p2[1]])
	for i in range(len(points)):
		# line coordinates, where (x1, y1) is upper left, and (x2, y2) bottom right
		# when i = 0, i-1 wraps around to last tile at index -1
		line_x1, line_x2 = sorted([points[i-1][0], points[i][0]])
		line_y1, line_y2 = sorted([points[i-1][1], points[i][1]])
		# if line is horizontal and has any non-border overlap with rectangle
		if (rect_y1 < line_y1 == line_y2 < rect_y2) and (rect_x1 < line_x2 and line_x1 < rect_x2):
			return False
		# if line is vertical and has any non-border overlap with rectangle
		if (rect_x1 < line_x1 == line_x2 < rect_x2) and (rect_y1 < line_y2 and line_y1 < rect_y2):
			return False
	return True

part_1 = part_2 = 0
for point1, point2 in combinations(points, 2):
	area = (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)
	part_1 = max(part_1, area)
	if area > part_2 and no_lines_overlap_with_rect(point1, point2):
		part_2 = max(part_2, area)

print("Part 1:", part_1)
print("Part 2:", part_2)
