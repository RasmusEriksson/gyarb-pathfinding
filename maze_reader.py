import matplotlib.image as img
import math
from time import perf_counter


image = img.imread("./mazes/maze_test.png")
dimensions = image.shape

dim_y = dimensions[0]
dim_x = dimensions[1]

#struktur: [0] = y, [1] = x
directions = [
    [-1,-1],
    [-1,0],
    [-1,1],
    [0,-1],
    [0,1],
    [1,-1],
    [1,0],
    [1,1],
]


#basklass för hörn
class node:
    def __init__(self,x,y):
        self.neighbors = []
        self.previous = None
        self.accessible = True

        self.x = x
        self.y = y

#klass för hörn inom Dijkstra's algoritm
class node_dijk(node):
    def __init__(self,y,x):
        super().__init__(y,x)
        self.distance = math.inf

def get_color(rgba):
    if rgba[0] == 1 and rgba[1] == 1:
        return "white"
    elif rgba[0] == 0 and rgba[1] == 0:
        return "black"
    elif rgba[0] == 1 and rgba[1] == 0:
        return "red"
    elif rgba[0] == 0 and rgba[1] == 1:
        return "green"

#Struktur för att få hörn från matris: maze[y][x]
def create_maze_dijk():
    print(dimensions)

    maze = []
    nodes = []
    start = None
    target = None

    for y in range(0,dim_y):
        maze.append([])
        for x in range(0,dim_x):
            color = get_color(image[y][x])
            print(x,y)
            new_node = node_dijk(y,x)
            
            if color == "black":
                new_node.accessible = False
            elif color == "green":
                start = new_node
                new_node.distance = 0
            elif color == "red":
                target = new_node
            
            maze[y].append(new_node)
            nodes.append(new_node)
    
    for y in range(0,dim_y):
        for x in range(0,dim_x):
            node = maze[y][x]
            node_pos = [node.y,node.x]

            for direction in directions:
                new_pos = [node_pos[0] + direction[0],node_pos[1] + direction[1]]

                if new_pos[0] > 0 and new_pos[0] <= dim_y - 1 and new_pos[1] > 0 and new_pos[1] <= dim_x - 1:
                    neighbor = maze[new_pos[0]][new_pos[1]]
                    if neighbor.accessible:
                        node.neighbors.append(neighbor)
    
    return maze, nodes, start, target
"""
start_time = perf_counter()

def execution_time_print(s,decimal):
    ms = s * 1000
    precision = math.pow(10,decimal)
    ms = math.floor(ms * precision) / precision

    print(f"This program took {ms} ms (milliseconds) to execute!")

execution_time = perf_counter() - start_time
execution_time_print(execution_time,4)
"""