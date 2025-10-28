def problem1():

    GRID_SIZE = 20

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
    
    return GRID_SIZE, obstacles