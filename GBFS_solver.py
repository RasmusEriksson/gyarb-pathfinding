import maze_reader
import math
from time import perf_counter

maze, unvisited, start, target = maze_reader.create_maze_gbfs()

queue = [start]

def print_maze(current):
    if current:
        print("exploring: ",[current.y,current.x])
    for row in maze:
        row_top = ""
        row_print = ""
        for square in row:
            row_top += "   "
            print_add = "  "
            
            
            if square == current:
                print_add += "🔍 "
            elif square == target:
                print_add += "🟥 "
            elif square == start:
                print_add += "🟩 "
            elif not square.accessible:
                print_add += "🔲 "
            elif square.is_path:
                print_add += "🔹 " 
            elif square.heuristic != math.inf:
                value = math.floor(square.heuristic)
                if value < 10:
                    value = "0"+str(value)
                print_add += str(value)+" "
            else:
                print_add += "  "
            
            row_print += print_add
        print(row_top)
        print(row_print)


def explore_node(node):
    
    #print_maze(node)
    for neighbor in node.neighbors:
        if neighbor in unvisited and not neighbor in queue:
            neighbor.calculate_h(target)
            neighbor.previous = node
            queue.append(neighbor)
    queue.remove(node)
    unvisited.remove(node)

def solve_maze():
    current_node = None

    while current_node != target and len(queue) > 0:
        lowest_heuristic = math.inf

        for node in queue:
            if node.heuristic < lowest_heuristic:
                current_node = node
                lowest_heuristic = node.heuristic
        
        if current_node and current_node in unvisited:
            explore_node(current_node)

    if current_node == target:
        print("Path found!")

        path = [current_node]

        previous = current_node.previous

        while previous:
            previous.is_path = True
            path.append(previous)
            current_node = previous
            previous = current_node.previous

    else:
        print("Path not found.")

def execution_time_print(s,decimal):
    ms = s * 1000
    precision = math.pow(10,decimal)
    ms = math.floor(ms * precision) / precision

    print(f"This program took {ms} ms (milliseconds) to execute!")

start_time = perf_counter()

solve_maze()

execution_time = perf_counter() - start_time
execution_time_print(execution_time,5)
print_maze(None)

