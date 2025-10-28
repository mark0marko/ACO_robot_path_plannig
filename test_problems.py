def problem1():

    GRID_SIZE = 20
    GOAL = (19, 19)


    obstacles = {(i, 1) for i in range(1, 3)} | \
            {(j, 2) for j in range(1, 3)} | \
            {(i, 14) for i in range(0, 4)} | \
            {(i, 15) for i in range(0, 4)} | \
            {(j, 5) for j in range(1, 4)} | \
            {(j, 6) for j in range(1, 4)} | \
            {(j, 7) for j in range(1, 4)} | \
            {(j, 8) for j in range(1, 4)} | \
            {(6, j) for j in range(0, 8)} | \
            {(7, j) for j in range(0, 8)} | \
            {(8, j) for j in range(0, 8)} | \
            {(10, j) for j in range(7, 12)} | \
            {(11, j) for j in range(7, 15)} | \
            {(12, j) for j in range(7, 15)} | \
            {(13, j) for j in range(7, 15)} | \
            {(j, 10) for j in range(7, 10)} | \
            {(j, 11) for j in range(7, 10)} | \
            {(i, 15) for i in range(6, 12)} | \
            {(i, 16) for i in range(6, 12)} | \
            {(i, 17) for i in range(10, 12)} | \
            {(i, 18) for i in range(10, 12)} | \
            {(i, 19) for i in range(10, 12)} | \
            {(i, 18) for i in range(14, 15)} | \
            {(i, 12) for i in range(15, 19)} | \
            {(i, 13) for i in range(15, 19)} | \
            {(i, 14) for i in range(15, 19)} | \
            {(i, 16) for i in range(17, 19)} | \
            {(i, 17) for i in range(17, 19)}

    return GRID_SIZE, obstacles, GOAL

def problem2():

    GRID_SIZE = 16
    GOAL = (13, 15)

    obstacles = {(i, 1) for i in range(1, 4)} | \
            {(i, 2) for i in range(1, 4)} | \
            {(i, 1) for i in range(6, 15)} | \
            {(i, 2) for i in range(6, 15)} | \
            {(i, 5) for i in range(1, 4)} | \
            {(i, 6) for i in range(1, 5)} | \
            {(i, 7) for i in range(1, 5)} | \
            {(i, 8) for i in range(1, 4)} | \
            {(7, j) for j in range(4, 8)} | \
            {(8, j) for j in range(4, 8)} | \
            {(10, j) for j in range(4, 8)} | \
            {(11, j) for j in range(4, 8)} | \
            {(13, j) for j in range(4, 8)} | \
            {(14, j) for j in range(4, 8)} | \
            {(i, 11) for i in range(1, 6)} | \
            {(i, 12) for i in range(1, 6)} | \
            {(i, 13) for i in range(2, 5)} | \
            {(8, j) for j in range(9, 12)} | \
            {(9, j) for j in range(9, 12)} | \
            {(10, j) for j in range(9, 12)} | \
            {(12, j) for j in range(9, 12)} | \
            {(13, j) for j in range(9, 12)} | \
            {(14, j) for j in range(9, 12)} | \
            {(i, 13) for i in range(10, 11)} | \
            {(i, 13) for i in range(14, 15)} | \
            {(i, 14) for i in range(7, 8)} | \
            {(i, 14) for i in range(9, 12)} | \
            {(i, 14) for i in range(13, 16)} | \
            {(i, 15) for i in range(0, 8)}

    return GRID_SIZE, obstacles, GOAL


def problem3():

    GRID_SIZE = 18
    GOAL = (17, 17)

    obstacles = {(i, 7) for i in range(1, 9)} | \
            {(i, 8) for i in range(1, 9)} | \
            {(i, 6) for i in range(4, 6)} | \
            {(i, 6) for i in range(12, 14)} | \
            {(i, 7) for i in range(11, 15)} | \
            {(i, 8) for i in range(12, 14)} | \
            {(1, j) for j in range(1, 5)} | \
            {(2, j) for j in range(1, 5)} | \
            {(3, j) for j in range(1, 5)} | \
            {(6, j) for j in range(1, 4)} | \
            {(7, j) for j in range(1, 4)} | \
            {(8, j) for j in range(1, 4)} | \
            {(9, j) for j in range(1, 5)} | \
            {(11, j) for j in range(1, 5)} | \
            {(12, j) for j in range(1, 5)} | \
            {(13, j) for j in range(1, 5)} | \
            {(14, j) for j in range(2, 4)} | \
            {(16, j) for j in range(0, 8)} | \
            {(17, j) for j in range(0, 8)} | \
            {(16, j) for j in range(10, 16)} | \
            {(17, j) for j in range(10, 16)} | \
            {(1, j) for j in range(10, 17)} | \
            {(2, j) for j in range(11, 16)} | \
            {(3, j) for j in range(10, 17)} | \
            {(6, j) for j in range(10, 17)} | \
            {(7, j) for j in range(11, 16)} | \
            {(8, j) for j in range(10, 17)} | \
            {(10, j) for j in range(11, 13)} | \
            {(11, j) for j in range(10, 17)} | \
            {(12, j) for j in range(10, 17)} | \
            {(13, j) for j in range(10, 17)} | \
            {(14, j) for j in range(15, 17)}

    return GRID_SIZE, obstacles, GOAL

def problem4():

    GRID_SIZE = 20
    GOAL = (19, 19)

    obstacles = {(i, 1) for i in range(1, 3)} | \
            {(i, 2) for i in range(1, 3)} | \
            {(i, 3) for i in range(6, 9)} | \
            {(i, 4) for i in range(11, 14)} | \
            {(i, 5) for i in range(1, 4)} | \
            {(i, 5) for i in range(15, 18)} | \
            {(i, 6) for i in range(15, 18)} | \
            {(i, 7) for i in range(6, 9)} | \
            {(i, 8) for i in range(10, 14)} | \
            {(i, 9) for i in range(10, 14)} | \
            {(i, 10) for i in range(10, 14)} | \
            {(i, 9) for i in range(4, 6)} | \
            {(i, 10) for i in range(4, 6)} | \
            {(i, 12) for i in range(11, 14)} | \
            {(i, 13) for i in range(11, 14)} | \
            {(i, 14) for i in range(11, 14)} | \
            {(i, 14) for i in range(2, 4)} | \
            {(i, 14) for i in range(15, 19)} | \
            {(i, 15) for i in range(2, 4)} | \
            {(i, 16) for i in range(10, 12)} | \
            {(i, 16) for i in range(17, 19)} | \
            {(i, 17) for i in range(10, 12)} | \
            {(i, 17) for i in range(17, 19)} | \
            {(3, j) for j in range(6, 8)} | \
            {(6, j) for j in range(4, 7)} | \
            {(11, j) for j in range(2, 5)} | \
            {(13, j) for j in range(2, 5)} | \
            {(15, j) for j in range(12, 14)} | \
            {(14, j) for j in range(17, 19)}

    return GRID_SIZE, obstacles, GOAL