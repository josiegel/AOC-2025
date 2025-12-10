import time
import math

def get_input(input):
    output = []
    with open(input, 'r') as file:
        for line in file:
            output.append(list(line.strip()))
    return output

def run_splitter(grid):
    splits = 0
    for i in range(len(grid)-1):
        for j in range(len(grid[i])):
            if grid[i-1][j] == 'S' or grid[i-1][j] == '|':
                if grid[i][j] == '^':
                    splits += 1
                    grid[i][j+1] = '|'
                    grid[i][j-1] = '|'
                else:
                    grid[i][j] = '|'
    return splits
            


def main():
    input = get_input('input.txt')
    splits = run_splitter(input)
    print(splits)



start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")