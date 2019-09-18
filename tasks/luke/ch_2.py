from ch_1_the_field import plotting, image, png

L = [[2,2],[3,2], [1.75,1], [2,1], [2.25,1], [2.5,1], [2.75, 1], [3,1], [3.25,1]]

# task 2.3.2
def task_2_3_2():
    plotting.plot(L, 4)

# task 2.4.3
def add2(vector, update):
    return [vector[0] + update[0], vector[1] + update[1]]

def scale_vec(vector, scale):
    return [x*scale for x in vector]

def task_2_4_3():
    translation = [1,2]
    updated = [add2(item, translation) for item in L]
    plotting.plot(updated, 6)

# task 2.5.4
def vec_mult(vector, scalar):
    multiplied = [x*scalar for x in vector]
    return multiplied 

def task_2_5_4():
    plotting.plot(scale(L, 0.5), 5)
    plotting.plot(scale(L, -0.5), 5)

# task 2.6.9
def segment(pt1, pt2, factor):
    mid_pt1 = vec_mult(pt1, factor) 
    mid_pt2 = vec_mult(pt2, 1 - factor)
    scaled = add2(mid_pt1,mid_pt2)
    return scaled

def task_2_6_9():
    one_vec = [2,4]
    two_vec = [4,8]
    factors = [x/100 for x in range(100)]
    segmented_points = [segment([3.5,3], [0.5,1], x) for x in factors]
    print(segmented_points)
    plotting.plot(segmented_points, 10)

if __name__ == "__main__":
    # task_2_3_2()
    # task_2_4_3()
    # task_2_5_4()
    task_2_6_9()
