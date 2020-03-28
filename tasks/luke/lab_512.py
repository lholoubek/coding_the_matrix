import numpy as np
from PIL import Image
import cv2
import os

def move_to_board(q):
    # takes a 3-vector q - a vector in whiteboard coordinates
    # returns a 3-vector p - a vector in whiteboard coordinates such that 
    # a line on the whiteboard traveling through point q intersects the whiteboard at point p
    return np.array([q[0]/q[2], q[1]/q[2], q[2]/q[2]])

def make_equations(x1, x2, w1, w2):
    # h as a D vector --> [y1x1, y2x1, y3x1, y1x2, y2x2, y3x2, y1x3, y2x3, y3x3]
    eq_1 = [-x1, 0, w1*x1, -x2, 0, w1*x2, -1, 0, w1]
    eq_2 = [0, -x1, w2*x1, 0, -x2, w2*x2, 0, -1, w2]
    return np.array([eq_1, eq_2])

def make_all_equations(corners):
    # takes known corners expressed as [x1, x2, w1, w2]
    # returns a matrix containing equations such that matrix row * h = 0
    # adds a D vector to the bottom of the matrix with 1 y1,x1 position 
    # for each known corner, process with make equations and add to L
    row_list = []
    for corner in corners:
        labels = ['x1', 'x2', 'w1', 'w2']    
        labeled_corner = dict(zip(labels, corner))
        rows = make_equations(labeled_corner['x1'], 
                              labeled_corner['x2'],
                              labeled_corner['w1'],
                              labeled_corner['w2'])
        row_list.append(rows[0])
        row_list.append(rows[1])
    
    # add the bottom row
    row_list.append(np.array([1,0,0,0,0,0,0,0,0]))
    concat_rows = np.concatenate(row_list, axis=0)
    L = np.reshape(concat_rows, (-1, 9))
    return L

def main():
    top_left = [358, 36, 0,0]
    bottom_left = [329,597, 0, 1]
    top_right = [592, 157, 1, 0]
    bottom_right = [580,483, 1, 1]
    known_corners = [top_left, bottom_left, top_right, bottom_right]
    L = make_all_equations(known_corners) 

    b = np.array([0,0,0,0,0,0,0,0,1]) # the system of equations all equal 0 except the last element
    # print(L)
    h = np.linalg.solve(L, b)
    # convert back to square matrix where x1, x2, x3 are columns and y1, y2, y3 are rows
    H = h.reshape([3,3]).T
    print(h)

    image_path = os.path.join(os.getcwd(), "board.png")
    whiteboard_image = Image.open(image_path)
    whiteboard_array = np.array(whiteboard_image)
    import pdb;pdb.set_trace()

if __name__ == '__main__':
    # test = [6, 9, 3] 
    # print(move_to_board(np.array(test)))
    # print(make_equations())
    main()

    