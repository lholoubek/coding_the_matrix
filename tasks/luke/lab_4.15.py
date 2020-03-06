import os
import numpy as np
from PIL import Image
import PIL
import cv2
import matplotlib.pyplot as plt
import math

def main():
    image_path = os.path.join(os.path.expanduser("~"), "Desktop/converted_3.png")
    # img = cv2.imread(image_path)
    image = Image.open(image_path) 
    rotate_t = rotate(90)
    print(rotate_t)
    print(T_to_pil(image.size, rotate_t))
    transformed = image.transform((image.size[0] * 2, image.size[1]*2), PIL.Image.AFFINE, data=T_to_pil(image.size, rotate_t)) 
    transformed.show()

def T_to_pil(size, transform):
    # converts a transformation matrix into the form required by PIL
    # see https://stackabuse.com/affine-image-transformations-in-python-with-numpy-pillow-and-opencv/

    # recenter resultant image
    T_pos1000 = np.array([
        [1, 0, size[0]],
        [0, 1, size[1]],
        [0, 0, 1]])
    # scale
    T_scale = np.array([
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 1]])
    # center original to 0,0
    T_recenter = np.array([
        [1, 0, -(size[0]/2)],
        [0, 1, -(size[1]/2)],
        [0, 0, 1]])
    T = T_pos1000 @ transform @ T_scale @ T_recenter 

    # get the inverse
    t_inv = np.linalg.inv(T)
    # flatten it because Pillow is weird
    converted = t_inv.flatten()[:6]
    return converted

def rotate(theta):
    theta_rad = math.radians(theta)
    T_rotate = np.array([
    [math.cos(theta_rad), -(math.sin(theta_rad)), 0],
    [math.sin(theta_rad), math.cos(theta_rad), 0],
    [0, 0, 1]])
    return T_rotate

def get_translation(alpha, beta):
    # alpha translates x, beta translates y
    pass

def get_scaling(alpha, beta):
    pass

if __name__ == "__main__":
    main()