class Rectangle:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.right = left + width
        self.bottom = top + height


user_input_1 = [float(num) for num in input().split()]
user_input_2 = [float(num) for num in input().split()]
rectangle_1 = Rectangle(user_input_1[0], user_input_1[1], user_input_1[2], user_input_1[3])
rectangle_2 = Rectangle(user_input_2[0], user_input_2[1], user_input_2[2], user_input_2[3])
if rectangle_1.left >= rectangle_2.left and rectangle_1.right <= rectangle_2.right and \
        rectangle_1.top <= rectangle_2.top and rectangle_1.bottom <= rectangle_2.bottom:
    print('Inside')
else:
    print('Not inside')