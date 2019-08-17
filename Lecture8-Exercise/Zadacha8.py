##Boxes
import math

class Box:
    def __init__(self, upper_left, upper_right, bottom_left, bottom_right):
        self.upper_left = upper_left
        self.upper_right = upper_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y


    @staticmethod
    def cal_distance(point_1, point_2):
        side_a = abs(point_1.x - point_2.x)
        side_b = abs(point_1.y - point_2.y)
        distance = math.sqrt(side_a ** 2 + side_b ** 2)
        return distance

    @staticmethod
    def calculate_perimeter(width, height):
        return 2 * width + 2 * height

    @staticmethod
    def calculate_area(width, height):
        return width * height


user_input = input()
points = []

while user_input != 'end':
    data = user_input.split(' | ')
    for item in data:
        x, y = item.split(':')
        x = int(x)
        y = int(y)
        points.append(Point(x,y))
    width = Point.cal_distance(points[0], points[1])
    height = Point.cal_distance(points[0], points[2])
    print(f'Box: {width:.0f}, {height:.0f}')
    perimeter = Point.calculate_perimeter(width,height)
    print(f'Perimeter: {perimeter:.0f}')
    area = Point.calculate_area(width,height)
    print(f'Area: {area:.0f}')
    user_input = input()
    points = []


