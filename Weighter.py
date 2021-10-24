import random
from random import randint

def main():
    graph_height = 25
    graph_width = graph_height

    base_weight = 25

    adjacency_matrix = [[None for i in range(graph_width)] for j in range(graph_height)]

    for i in range(graph_height):

        x, y = node_coord(i)

        neighbors = []
        # diag = []

        north = node_id(x, y-1)
        south = node_id(x, y+1)
        east = node_id(x+1, y)
        west = node_id(x-1, y)

        for direction in [north, south, east, west]:

            if direction is None or random.randint(0, 100) > 80:
                continue

            neighbors.append(direction)
        
        northe = node_id(x+1, y-1)
        southe = node_id(x+1, y+1)
        northw = node_id(x-1, y-1)
        southw = node_id(x-1, y+1)

        for direction in [northe, southe, northw, southw]:

            if direction is None or random.randint(0, 100) < 90:
                continue

            neighbors.append(direction)

        for neighbor in neighbors:

            adjacency_matrix[i][neighbor] = base_weight + randint(-20, 2)
    
    for i in range(graph_height):

        adjacency_matrix[i][i] = 0
    
    for row in adjacency_matrix:
        print(str(row) + ',')
        

def node_id(x, y, width=5):

    if x >= width or y >= width or x < 0 or y < 0:
        return None

    n_id = x + y * width

    return n_id

def node_coord(id, width=5):

    node_x = id % width
    node_y = id // width

    return (node_x, node_y)

# for row in adjacency_matrix:

#     kill = random.randint(0, 24)
#     row[kill] = None

main()



# print(float('inf') == float('inf'))

    



