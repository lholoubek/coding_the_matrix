import image_mat_util as imu
import matutil as mu
import math

# Task 4.15.1
loc_matrix, color_matrix = imu.file2mat("icon_small.png")
# imu.mat2display(loc_matrix, color_matrix, xmin=-50, scale=2, crosshairs=True)

# Task 4.15.2
def identity():
    return mu.Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), {('x', 'x'): 1, ('y', 'y'): 1, ('u', 'u'): 1})

# print(identity())
# test_loc_matrix = mu.Mat(({'x', 'y', 'u'}, {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)}), {('x', (1, 0)): 1, ('y', (1, 0)): 1, ('x', (1, 1)): 3, ('y', (1, 1)): 3, ('x', (2, 2)): 5, ('y', (2, 2)): 5})
# test_col_matrix = mu.Mat(({'b', 'g', 'r'}, {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)}), {('b', (1, 0)): 50, ('g', (1, 0)): 50, ('r', (1, 0)): 50, ('b', (1, 1)): 120, ('g', (1, 1)): 120, ('r', (1, 1)): 120, ('b', (2, 2)): 200, ('g', (2, 2)): 200, ('r', (2, 2)): 200})
test_loc_matrix= mu.Mat(({'x', 'y', 'u'}, {(0, 0), (0, 1)}), {('x', (0, 0)):2, ('y', (0, 1)):3})
# print(test_loc_matrix)
# print(test_col_matrix)
# adjusted_loc_matrix = identity() * test_loc_matrix
# print(adjusted_loc_matrix)
# imu.mat2display(adjusted_loc_matrix, test_col_matrix)

# if adjusted_loc_matrix == test_loc_matrix:
#    print("they're the same")

# adjusted_graphic = identity() * loc_matrix
# imu.mat2display(adjusted_graphic, color_matrix)

# Task 4.15.3
def translation(alpha, beta):
    return_mat = identity()
    return_mat['x', 'u'] = alpha
    return_mat['y', 'u'] = beta
    return return_mat
    # return mu.Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), {('x', 'u'): alpha, ('y', 'u'): beta})
# print(translation(13, 15))
# print(translation(13, 15) * test_loc_matrix)
# adjusted_graphic = translation(13, 15) * loc_matrix
# imu.mat2display(adjusted_graphic, color_matrix, scale=2)

# Task 4.15.4
def scale(alpha, beta):
    return mu.Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), {('x', 'x'): alpha, ('y', 'y'): beta})

# adjusted_graphic = scale(2, 3) * loc_matrix
# imu.mat2display(adjusted_graphic, color_matrix, scale=2)

# Task 4.15.5
def rotation(theta):
    # 1, 0 - > root3/2, 1/2
    return mu.Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), {('x', 'x'): math.cos(theta), ('y', 'x'): math.sin(theta), ('y', 'y'): math.cos(theta), ('x', 'y'): -math.sin(theta), ('u', 'u'): 1})
# print(rotation(math.radians(45)))
# adjusted_graphic = rotation(math.radians(15)) * loc_matrix
# imu.mat2display(adjusted_graphic, color_matrix, xmin=-20, scale=2, crosshairs=True)

# Task 4.15.6
def rotation_about(theta, x, y):
    m = translation(-x, -y)
    print(m)
    trans_with_rot = m * rotation(theta)
    print(rotation(theta))
    print(trans_with_rot)
    restored_rot = trans_with_rot * translation(x, y)
    print("restored rot:", restored_rot)
    return restored_rot

# adjusted_graphic = rotation_about(math.radians(30), 5, 5) * loc_matrix
# imu.mat2display(adjusted_graphic, color_matrix, xmin=-20, scale=2, crosshairs=True)

# Task 4.15.7
def reflect_y():
    return mu.Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), {('x', 'x'): -1, ('y', 'y'): 1, ('u', 'u'): 1})

# Task 4.15.8
def reflect_x():
    return mu.Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), {('x', 'x'): 1, ('y', 'y'): -1, ('u', 'u'): 1})

# Task 4.15.9
def scale_color(r, g, b):
    return mu.Mat(({'r', 'g', 'b'}, {'r', 'g', 'b'}), {('r', 'r'): r, ('g', 'g'): g, ('b', 'b'): b})

# Task 4.15.10
def grayscale():
    return mu.Mat(({'r', 'g', 'b'}, {'r', 'g', 'b'}), {('r', 'r'): 77/256, ('r', 'g'): 151/256, ('r', 'b'): 28/256, ('g', 'r'): 77/256, ('g', 'g'): 151/256, ('g', 'b'): 28/256, ('b', 'r'): 77/256, ('b', 'g'): 151/256, ('b', 'b'): 28/256})

# Task 4.14.11
def reflect_about(x1, y1, x2, y2):
    # trans_to_center = translation(-(x1 - x2)/2, -(y1-y2)/2)
    # corrected_rotation = rotation(math.atan((x1-x2)/(y1-y2))
    # re_rotate = rotation(-1 * math.atan((x1-x2)/(y1-y2))
    # re_trans = translation((x1 - x2)/2, (y1-y2)/2)
    return translation(-(x1 - x2)/2, -(y1-y2)/2) * rotation(math.atan((x1-x2)/(y1-y2))) * reflect_y() * rotation(-1 * math.atan((x1-x2)/(y1-y2))) * translation((x1 - x2)/2, (y1-y2)/2)

adjusted_graphic = reflect_about(5, 3, 7, 15) * loc_matrix
# adjusted_color = scale_color(3, 1, 1) * color_matrix
grey = grayscale() * color_matrix
imu.mat2display(adjusted_graphic, grey, xmin=-50, ymin=-50, scale=2, crosshairs=True)