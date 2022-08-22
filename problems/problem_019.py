# Complete the is_inside_bounds function which has the
# following parameters:
#   x: the x coordinate to check
#   y: the y coordinate to check
#   rect_x: The left of the rectangle
#   rect_y: The bottom of the rectangle
#   rect_width: The width of the rectangle
#   rect_height: The height of the rectangle
#
# The is_inside_bounds function returns true if all of
# the following are true
#   * x is greater than or equal to rect_x
#   * y is greater than or equal to rect_y
#   * x is less than or equal to rect_x + rect_width
#   * y is less than or equal to rect_y + rect_height

# check if


def is_inside_bounds(x, y, rect_x, rect_y, rect_width, rect_height):
    if (x >= rect_x and x <= rect_x + rect_width) and (
        y >= rect_y and y <= rect_y + rect_height
    ):
        return True
    else:
        return False


print(is_inside_bounds(5, 5, 1, 1, 2, 2))
print(is_inside_bounds(5, 5, 1, 1, 4, 4))
print(is_inside_bounds(5, 5, 5, 3, 1, 1))
print(is_inside_bounds(10, 15, 10, 15, 6, 6))
print(is_inside_bounds(10, 5, 5, 10, 10, 5))
print(is_inside_bounds(10, 10, 5, 5, 6, 6))
