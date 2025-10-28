import numpy as np
import matplotlib.pyplot as plt
import random

from test_problems import problem2

START = (0, 0)

GRID_SIZE, obstacles, GOAL = problem2()

# ACO parameters
num_ants = 30
num_iterations = 50
alpha = 2.0                             # pheromone influence
beta = 1.0                              # heuristic influence
evaporation_factor = 0.3
Q = 100.0

rho = 1 - evaporation_factor

pheromone = np.ones( ( GRID_SIZE, GRID_SIZE ) )

def find_neighbors( cell ):
    x, y = cell
    directions = [
        (1,0), (-1,0), (0,1), (0,-1),
        (1, 1), (-1, -1), (1, -1), (-1, 1)
    ]

    result = []

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and (nx, ny) not in obstacles:
            if abs(dx) + abs(dy) == 2:
                step_cost = 1.41
            else:
                step_cost = 1.0

            result.append( ( (nx, ny), step_cost ) )

    return result

best_path = None
best_cost = float('inf')
last_best_cost = float('inf')

for iter in range(num_iterations):
    all_paths = []
    all_costs = []

    for _ in range(num_ants):
        path = [START]
        visited = {START}
        path_cost = 0

        while path[-1] != GOAL:
            neighbors = [ n for n in find_neighbors( path[-1] ) if n[0] not in visited ]
            if not neighbors: break

            probs = []

            for ( n, step_cost ) in neighbors:
                tau = pheromone[n]
                eta = 1.0 / step_cost
                probs.append( (tau ** alpha) * (eta ** beta) )

            probs = np.array( probs ) / sum( probs )

            next_cell, move_cost = random.choices( neighbors, weights=probs )[0]

            path_cost += move_cost

            path.append( next_cell )
            visited.add( next_cell )

        if path[-1] == GOAL:
            all_paths.append(path)
            all_costs.append(path_cost)

            if path_cost < best_cost:
                best_cost = path_cost
                best_path = path

    # Evaporate pheromone
    pheromone = rho * pheromone

    # Deposit pheromone
    for path, cost in zip( all_paths, all_costs ):
        for cell in path:
            pheromone[cell] += Q / cost

    if best_cost < last_best_cost:
        print(f"Iteration {iter + 1}: Best cost = {best_cost if best_path else 'No path found'}")
        last_best_cost = best_cost

grid = np.zeros((GRID_SIZE, GRID_SIZE))

for ox, oy in obstacles:
    grid[ox, oy] = -1

plt.figure(figsize=(6,6))
plt.imshow(grid.T, cmap='Greys', origin='lower')

if best_path:
    xs, ys = zip(*best_path)
    plt.plot(xs, ys, color='red', linewidth=2)
    plt.scatter(*START, color='green', s=100, label='Start')
    plt.scatter(*GOAL, color='blue', s=100, label='Goal')
    plt.legend()
    print(f"Best path cost: {best_cost:2f}")
else:
    print("No path found!")

ax = plt.gca()
ax.set_xticks(np.arange(-0.5, GRID_SIZE, 1), minor=True)
ax.set_yticks(np.arange(-0.5, GRID_SIZE, 1), minor=True)
ax.grid(which='minor', color='magenta', linestyle='-', linewidth=1)

ax.set_xticks([])
ax.set_yticks([])

plt.gca().invert_yaxis()
plt.title(f"ACO Path (Cost: {best_cost:2f})")
plt.show()
