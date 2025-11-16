import os
import numpy as np
import matplotlib.pyplot as plt
import random

from test_problems import problem2

START = ( 0, 0 )
GRID_SIZE, obstacles, GOAL = problem2()

dynamic_schedule = {
    25: {'add': [ (0,5),(9,5) ], 'remove': []},
    # 40: {'add': [(5,5), (5,6), (6,5), (6,6)], 'remove': []},
    50: {'add': [(5,5), (5,6), (6,5), (6,6)], 'remove': [ ]},
    70: {'add': [(12,5)], 'remove': [ (9,5), (5,5), (5,6), (6,5), (6,6) ]},
    85: {'add': [], 'remove': []}
}

people = [
    {'pos':[4, 5], 'heading':1, 'direction': True },    #direction --> True: UP-DOWN; False: LEFT-RIGHT
    {'pos':[4, 10], 'heading':1, 'direction': False },
    {'pos':[6, 5], 'heading':-1, 'direction': False },
    # {'pos':[6, 6], 'heading':-1, 'direction': True },
    # {'pos':[8, 12], 'heading':-1, 'direction': True },
    {'pos':[8, 12], 'heading':-1, 'direction': False },
    {'pos':[11, 10], 'heading':1, 'direction': True }
]

def update_people():
    for p in people:
        if p['direction']:
            p['pos'][1] += p['heading']

            if p['pos'][1] <= 0 or p['pos'][1] >= GRID_SIZE-1:
                p['heading'] *= -1

            if ( p['pos'][0], p['pos'][1] + p['heading'] ) in obstacles:
                p['heading'] *= -1
        else:
            p['pos'][0] += p['heading']

            if p['pos'][0] <= 0 or p['pos'][0] >= GRID_SIZE-1:
                p['heading'] *= -1

            if ( p['pos'][0] + p['heading'], p['pos'][1] ) in obstacles:
                p['heading'] *= -1


def get_people_positions():
    return [ tuple( p['pos'] ) for p in people ]

num_ants = 30
num_iterations = 120
alpha = 2.0
beta = 3.0
evaporation_factor = 0.1
Q = 100.0
rho = 1 - evaporation_factor

pheromone = np.ones( ( GRID_SIZE, GRID_SIZE ) )


def find_neighbors( cell, people_positions ):
    x, y = cell
    directions = [
        (1,0), (-1,0), (0,1), (0,-1),
        (1, 1), (-1, -1), (1, -1), (-1, 1)
    ]
    result = []
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            if ( nx, ny ) not in obstacles and ( nx, ny ) not in people_positions:
                step_cost = 1.41 if abs( dx ) + abs( dy ) == 2 else 1.0
                result.append( ( (nx, ny), step_cost ) )
    return result

def draw_current( iteration, people_positions, current_best_path, current_best_cost ):
    # os.makedirs("frames", exist_ok=True)

    plt.clf()

    plt.subplot( 1, 2, 1 )
    grid = np.zeros( ( GRID_SIZE, GRID_SIZE ) )
    for ox, oy in obstacles:
        grid[ox, oy] = -1
    plt.imshow( grid.T, cmap='Greys', origin='lower' )

    if current_best_path:
        xs, ys = zip( *current_best_path )
        plt.plot( xs, ys, color='red', linewidth=2 )

    plt.scatter( *START, color='green', s=100 )
    plt.scatter( *GOAL, color='blue', s=100 )

    for px, py in people_positions:
        plt.scatter( px, py, color='yellow', s=140 )

    ax = plt.gca()
    ax.set_xticks( np.arange(-0.5, GRID_SIZE, 1), minor=True )
    ax.set_yticks( np.arange(-0.5, GRID_SIZE, 1), minor=True )
    ax.grid( which='minor', color='magenta', linestyle='-', linewidth=1 )
    ax.set_xticks( [] )
    ax.set_yticks( [] )
    plt.gca().invert_yaxis()
    plt.title( f"Grid (Iter {iteration+1})" )

    plt.subplot( 1, 2, 2 )
    plt.imshow( pheromone.T, origin='lower' )
    plt.colorbar( label="pheromone level" )
    plt.title( "Pheromone Heatmap" )
    plt.gca().invert_yaxis()

    plt.suptitle( f"Iteration {iteration+1} — Best Cost: {current_best_cost:.2f}" )

    # plt.savefig(f"frames/frame_{iteration:03d}.png", dpi=150, bbox_inches='tight')
    plt.pause(0.01)

best_cost = float( 'inf' )
last_best_cost = float( 'inf' )

plt.figure( figsize=(6,6) )

for iter in range( num_iterations ):

    update_people()
    people_positions = get_people_positions()

    if iter in dynamic_schedule:
        changes = dynamic_schedule[iter]
        for obs in changes.get( 'add', [] ):
            obstacles.add( obs )
        for obs in changes.get( 'remove', [] ):
            obstacles.discard( obs )

    all_paths = []
    all_costs = []
    current_best_path = None
    current_best_cost = float( 'inf' )

    for _ in range( num_ants ):
        path = [START]
        visited = {START}
        path_cost = 0

        while path[-1] != GOAL:
            neighbors = [ n for n in find_neighbors( path[-1], people_positions ) if n[0] not in visited ]
            if not neighbors:
                break

            probs = []
            for ( n, step_cost ) in neighbors:
                tau = pheromone[n]
                eta = 1.0 / step_cost
                probs.append( ( tau ** alpha ) * ( eta ** beta ) )
            probs = np.array( probs )
            probs /= probs.sum()

            next_cell, move_cost = random.choices( neighbors, weights=probs )[0]
            path_cost += move_cost
            path.append( next_cell )
            visited.add( next_cell )

        if path[-1] == GOAL:
            all_paths.append( path )
            all_costs.append( path_cost )

            if path_cost < current_best_cost:
                current_best_cost = path_cost
                current_best_path = path

    # Evaporate pheromone
    pheromone = rho * pheromone
    # Deposit pheromone
    for path, cost in zip( all_paths, all_costs ):
        for cell in path:
            pheromone[cell] += Q / cost

    # draw best iteration
    draw_current( iter, people_positions, current_best_path, current_best_cost )

plt.show()
