from ch_1_the_field import plotting, image, png

S = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 +1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

def task_1_4_1():
    print(S)
    plotting.plot(s)

def task_1_4_3():
    transform = 1 + 2j # one unit in x, 2 in y
    transformed = {transform + z for z in S}
    plotting.plot(transformed, 6)

def task_1_4_7():
    transform = .5 # scalling down
    transformed = {transform * z for z in S}
    print(S)
    print(transformed)
    plotting.plot(transformed, 6)


if __name__ == "__main__":
    # task_1_4_1()
    # task_1_4_3()
    task_1_4_7()