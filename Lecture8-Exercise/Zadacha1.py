#01. Distance Between Points



import math


class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y


def calc_distance(self):
    side_a = abs(self.point_1.x - self.point_2.x)
    side_b = abs(self.point_1.y - self.point_2.y)
    side_c = math.sqrt(side_a ** 2 + side_b ** 2)
    return side_c


def create_point(x, y):
    point = Point(x,y)
    return point


x_1, y_1 = [int(num) for num in input().split()]
x_2, y_2 = [int(num) for num in input().split()]

point_1 = Point(x_1,y_1)
point_2 = Point(x_2,y_2)

print(f'{cal_distance(point_1, point_2):.3f}')


