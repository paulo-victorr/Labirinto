import time
from maze import Maze
from collections import deque

s = deque()


maze_csv_path = "labirinto1.txt"  
maze = Maze() 

maze.load_from_csv(maze_csv_path)

maze.run()
maze.init_player()




