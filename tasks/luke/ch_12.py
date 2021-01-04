import PIL
from PIL import Image
import os
import numpy as np
import math
from math import sqrt
import mat
import vec
from matplotlib import pyplot as plt
from matplotlib import cm
from statistics import mean 

FACES_DIR = "./eigenfaces/faces"
UNCLASSIFIED_DIR = "./eigenfaces/unclassified"

def main():
    unclassified_faces, unclassified_dimensions = load_column_images(UNCLASSIFIED_DIR)
    faces_original, dimensions = load_column_images(FACES_DIR)
    width, height = dimensions
    normalized_faces = normalize(faces_original)
    k = 10
    print("height: ", height)
    print("width: ", width)
    print("Faces are normalized. SVD time bb")
    u_mat, sig_arr, v_t = np.linalg.svd(normalized_faces, full_matrices=False)

    # first_row_v_t = reshape_column_vec(v_t[0], 166)
    # img = plt.imshow(first_row_v_t)
    # img.set_cmap("gray")
    # plt.show()

    eigen_face_basis= u_mat[:,:5]

    print("Distance of known faces:")
    distance_of_known_faces = []
    for face in range(normalized_faces.shape[1]):
        column_face = normalized_faces.T[face]
        distance = math.sqrt(distance_squared(eigen_face_basis, column_face))
        print("Face: {}, distance: {}".format(face, distance))
        distance_of_known_faces.append(distance)

    avg_distance_known_faces = mean(distance_of_known_faces)
    max_distance_known_faces = max(distance_of_known_faces)
    print("Average distance of known faces: {}".format(avg_distance_known_faces))
    print("Max distance known faces: {}".format(max_distance_known_faces))

    known_faces_average = faces_original.mean(axis=1)
    unknown_faces_distances = []
    for face in range(unclassified_faces.shape[1]):
        normalized_face = unclassified_faces.T[face] - known_faces_average
        distance = math.sqrt(distance_squared(eigen_face_basis, normalized_face))
        print("Face: {}, distance: {}".format(face, distance))
        unknown_faces_distances.append(distance)
        face_img = reshape_column_vec(unclassified_faces.T[face], 166)
        img = plt.imshow(face_img)
        img.set_cmap('gray')
        plt.show()
    
    print("Average distance of unknown faces: {}".format(mean(unknown_faces_distances)))
    print("min distance unkonwn faces: {}".format(min(unknown_faces_distances)))
        
    # reshaped = reshape_column_vec(eigen_face, 166)
    # img = plt.imshow(reshaped)
    # img.set_cmap("gray")
    # plt.show()


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def load_column_images(image_dir):
    # loads images from image_dur 
    # returns numpy array of images
    # each image is a single column vector
    images = os.listdir(image_dir)
    image_data = []
    dimensions = None
    for image in images:
        file_name = os.path.join(image_dir, image)
        pil_image = Image.open(file_name) 
        image_arr = np.array(pil_image)
        if len(image_arr.shape) > 2:
            image_arr = rgb2gray(image_arr)
        if dimensions is None:
            dimensions = (image_arr.shape[1],image_arr.shape[0])
        image_data.append(columnify_image(image_arr))

    image_columns = np.column_stack(image_data)
    return (image_columns, dimensions)

def columnify_image(image_arr):
    # rehapes a 2d image array into a single column vector
    column_vec_length = np.shape(image_arr)[0] * np.shape(image_arr)[1]
    reshaped = np.reshape(image_arr, (column_vec_length,))
    return reshaped

def normalize(image_arr):
    # takes in array with images as columns 
    # returns an array where the average is removed from all columns
    mean_vec = image_arr.mean(axis=1)
    mean_vec_extended = np.repeat(mean_vec, image_arr.shape[1])
    mean_mat = np.reshape(mean_vec_extended, (-1, image_arr.shape[1]))

    # orig_img = image_from_column_vec(image_arr.T[0], 166)
    # less_avg_vec = image_arr.T[0] - mean_vec
    # less_avg = image_from_column_vec(less_avg_vec, 166)
    # mean_img = image_from_column_vec(mean_vec, 166)
    # orig_img.show()
    # less_avg.show()
    # mean_img.show()

    # import pdb;pdb.set_trace()

    # subtract the mean vector from all of the individual columns
    normalized_image_arr = image_arr - mean_mat
    return normalized_image_arr
    
def image_from_column_vec(column_vec, width):
    # takes a np array column vector representing an image
    # returns a PIL Image with dimensions width,height
    reshaped_vec = reshape_column_vec(column_vec, width)
    image = Image.fromarray(np.uint8(cm.gray(reshaped_vec*255))).convert('RGB')
    return image

def reshape_column_vec(column_vec, width):
    return np.reshape(column_vec, (-1, width))


def get_test_mat_vec():
    test_mat = np.array([[1/math.sqrt(2), 1/math.sqrt(3)],
                         [1/math.sqrt(2), -1/math.sqrt(3)],
                         [0, 1/math.sqrt(3)]])
    test_vec = np.array([10,20,30])
    return (test_mat, test_vec)

def projected_rep(matrix, vec):
    projected = matrix @ vec 
    # import pdb;pdb.set_trace()
    return projected

def projection_length_squared(matrix, vec):
    projected = projected_rep(matrix.T, vec)
    projected_length_squared = np.linalg.norm(projected) ** 2
    return projected_length_squared

def distance_squared(matrix, vec):
    projected_length_squared = projection_length_squared(matrix, vec)
    vec_squared = np.dot(vec, vec)
    distance_squared = vec_squared - projected_length_squared 
    return distance_squared

if __name__ == "__main__":
    main()
    # test_arr = np.column_stack(([[2,4,6], [2,6,8], [2,8,10]]))
    # print(test_arr)
    # print(normalize(test_arr))

