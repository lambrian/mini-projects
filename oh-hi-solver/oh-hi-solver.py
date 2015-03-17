"""
Reads in file of starter board.
First line should be side length of board. 
Next n lines should represent the rows.
Red = R
Blue = B
Empty = E

"""
import sys

def read_grid (filename):
    f = open (filename, 'r')
    size = int(f.readline())
    print size * 2
    grid = [[0 for r in range(size)] for c in range(size)]
    
    for r in range(size):
        line = f.readline()
        for c in range(size):
            grid[r][c] = line[c]
    
   return grid

def main():
    grid = read_grid (sys.argv[1])
    
    
    

if __name__ == "__main__":
    main()
