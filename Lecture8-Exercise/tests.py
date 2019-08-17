import math


class Point:
    points= []

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{(self.x, self.y)}'

    @staticmethod
    def calculate_distance(point_1, point_2):
        side_a = abs(point_1.x - point_2.x)
        side_b = abs(point_1.y - point_2.y)
        distance = math.sqrt(side_a ** 2 + side_b ** 2)
        return distance

    @staticmethod
    def get_point():
        n = int(input())
        points = []
        while n > 0:
            n -= 1
            user_input = [int(x) for x in input().split()]
            current_point = Point(user_input[0], user_input[1])
            Point.points.append(current_point)
        return points

    @staticmethod
    def compare_distance():
        distance_list = []
        for i in range(len(Point.points)):
            for j in range(len(Point.points)):
                if i == j:
                    pass
                else:
                    segment = Point.points[i] , Point.points[j]
                    distance_list.append(segment)
        return distance_list

    @staticmethod
    def final_calculations():
        lowest_value = 222222222222
        lowest_point = []
        for item in Point.compare_distance():
            if Point.calculate_distance(item[0], item[1]) < lowest_value:
                lowest_value = Point.calculate_distance(item[0], item[1])
                lowest_point = [item[0], item[1]]
            else:
                pass
        return f'{lowest_value:.3f}\n{lowest_point[0]}\n{lowest_point[1]}'


Point.get_point()
Point.compare_distance()
print(Point.final_calculations())
