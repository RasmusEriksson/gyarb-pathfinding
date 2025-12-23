import maze_reader
import math

maze, unvisited, start, target = maze_reader.create_maze_dijk()

test_list = []

def explore_node(node):
    print("exploring: ",[node.y,node.x])
    for neighbor in node.neighbors:
        if neighbor in unvisited:
            x_difference = abs(node.x - neighbor.x)
            y_difference = abs(node.y - neighbor.y)

            added_distance = math.sqrt(math.pow(x_difference,2) + math.pow(y_difference,2))
            new_distance = node.distance + added_distance

            if new_distance < neighbor.distance:
                neighbor.distance = new_distance
                neighbor.previous = node
    unvisited.remove(node)

def solve_maze():
    current_node = None

    while current_node != target and len(unvisited) > 0:
        shortest_distance = math.inf

        for node in unvisited:
            if node.distance < shortest_distance:
                current_node = node
                shortest_distance = node.distance
        
        if current_node and current_node in unvisited:
            explore_node(current_node)

    if current_node == target:
        print("Path found!")
    else:
        print("Path not found.")

solve_maze()