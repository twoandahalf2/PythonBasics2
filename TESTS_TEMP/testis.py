
# coordinates in 2D space. Move the CalculateDistance() method in the Point class, exactly as it is.
# Then use “Point.CalculateDistance(point1, point2)” signature, to use the method.
# Create 2 methods in the Box class:
# CalculatePerimeter(width, height)
# CalculateArea(width, height).
# Make them return integers, representing the perimeter and area of the box.
# The formulas are respectively – (2 * Width + 2 * Height) and (Width * Height).
# The Width is the distance between the UpperLeft and the UpperRight Points, and ALSO – the Bottomleft and the BottomRight Points.
# The Height is the distance between the UpperLeft and the BottomLeft Points, and ALSO – the UpperRight and the BottomRight Points.
# You will receive several input lines in the following format:
# {X1}:{Y1} | {X2}:{Y2} | {X3}:{Y3} | {X4}:{Y4}
# Those will be the coordinates to UpperLeft, UpperRight, BottomLeft and BottomRight (IN THE SAME ORDER).
# When you receive the command “end”. You must print all Boxes in the following format:
# “Box: {width}, {height}
#  Perimeter: {perimeter}
#  Area: {area}”
import math


class Point:
    def __int__(self, x, y):
        self.x= x
        self.y = y

    @staticmethod
    def cal_distance(point_1, point_2):
        side_a = abs(point_1.x - point_2.x)
        side_b = abs(point_1.y - point_2.y)
        distance = math.sqrt(side_a ** 2 + side_b ** 2)
        return distance


class Box:
    def __init__(self, upperleft,upperright, bottomleft, bottomright):
        self.upperleft = upperleft
        self.upperright = upperright
        self.bottomleft = bottomleft
        self.bottomright = bottomright

    def calculate_perimeter(self):
        pass

    def calculate_area(self):
        pass

