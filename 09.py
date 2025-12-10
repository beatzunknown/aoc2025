from itertools import combinations

with open('09.txt', 'r') as f:
	# points are (x, y) tuples where top-left coord is (0, 0)
	points = [tuple(map(int, l.rstrip().split(','))) for l in f.readlines()]

'''
For part 2 there are 2 checks necessary to determine that a rectangle is
completely inside a polygon.
1. Are all corners inside the polygon? This can be done by raycasting from
   each corner in all 4 direction to find an intersection with the polygon.
   If no intersection in a direction, corner is not in polygon. Though there
   is an edge case where you may intersect with polygon but the corner is
   not inside. This edge case is for concave polygons.
2. Are there any polygon edges having a non-border overlap with rectangle?
   This will address the concave polygon edge case as is detects if there
   is a concavity in the rectangle, even if all 4 corners are in polygon.
'''

def any_lines_overlap_with_rect(p1, p2, include_border):
	# rectangle corner coordinates, where (x1, y1) is upper left, and (x2, y2) bottom right
	rect_x1, rect_x2 = sorted([p1[0], p2[0]])
	rect_y1, rect_y2 = sorted([p1[1], p2[1]])
	for i in range(len(points)):
		# line coordinates, where (x1, y1) is upper left, and (x2, y2) bottom right
		# when i = 0, i-1 wraps around to last tile at index -1
		line_x1, line_x2 = sorted([points[i-1][0], points[i][0]])
		line_y1, line_y2 = sorted([points[i-1][1], points[i][1]])
		# Border overlap check including border is for corner intersections (ray casting)
		if include_border:
			# if line is horizontal and has any overlap with rectangle
			if (rect_y1 <= line_y1 == line_y2 <= rect_y2) and (rect_x1 <= line_x2 and line_x1 < rect_x2):
				return True
			# if line is vertical and has any overlap with rectangle
			if (rect_x1 <= line_x1 == line_x2 <= rect_x2) and (rect_y1 <= line_y2 and line_y1 < rect_y2):
				return True
		# Non-border overlap check is to determine if any polygon line are INSIDE the
		# rectangle. Sharing border doesn't indicate any concavity.
		else:
			# if line is horizontal and has any non-border overlap with rectangle
			if (rect_y1 < line_y1 == line_y2 < rect_y2) and (rect_x1 < line_x2 and line_x1 < rect_x2):
				return True
			# if line is vertical and has any non-border overlap with rectangle
			if (rect_x1 < line_x1 == line_x2 < rect_x2) and (rect_y1 < line_y2 and line_y1 < rect_y2):
				return True
	return False

def all_corners_in_polygon(p1, p2):
	corners = [(p1[0], p1[1]), (p1[0], p2[1]), (p2[0], p1[1]), (p2[0], p2[1])]
	for corn_x, corn_y in corners:
		left_intersect = any_lines_overlap_with_rect((corn_x, corn_y), (0, corn_y), include_border=True)
		right_intersect = any_lines_overlap_with_rect((corn_x, corn_y), (float('inf'), corn_y), include_border=True)
		up_intersect = any_lines_overlap_with_rect((corn_x, corn_y), (corn_x, 0), include_border=True)
		down_intersect = any_lines_overlap_with_rect((corn_x, corn_y), (corn_x, float('inf')), include_border=True)
		if not (left_intersect and right_intersect and up_intersect and down_intersect):
			return False
	return True

part_1 = part_2 = 0
for point1, point2 in combinations(points, 2):
	area = (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)
	part_1 = max(part_1, area)
	if area > part_2 and not any_lines_overlap_with_rect(point1, point2, include_border=False) and all_corners_in_polygon(point1, point2):
		part_2 = max(part_2, area)
		print(part_2, point1, point2)

print("Part 1:", part_1)
print("Part 2:", part_2)
