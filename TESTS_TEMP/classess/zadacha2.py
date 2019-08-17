import math

class Point:

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def create_point(self):
        point = [self.x, self.y]
        return point

    @staticmethod
    def calculate_distance(point_1:[], point_2:[]):
        side_a = abs(point_1.x - point_2.x)
        side_b = abs(point_1.y - point_2.y)
        side_c = math.sqrt(side_a**2 + side_b**2)
        return side_c


n = int(input())

total_points = []

while n > 0:
    n -= 1
    a, b = [int(x) for x in input().split()]
    point = Point(a, b).create_point()
    total_points.append(point)

segment_list = []

for index_1 in range(len(total_points)):
    for index_2 in range(len(total_points)):
        if index_1 != index_2:
            segment = Point(total_points[index_1][0], total_points[index_2][0])
            segment_list.append(segment)