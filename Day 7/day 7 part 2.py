import time
from copy import deepcopy

def get_input(input):
    output = []
    with open(input, 'r') as file:
        for line in file:
            output.append(list(line.strip()))
    return output

def quantum_splitter(grid):
    for i in range(len(grid[0])):
        if grid[0][i] == 'S':
            grid[0][i] = 1
    for i in range(1,len(grid)):
        for j in range(len(grid[i])):
            if isinstance(grid[i-1][j], int):
                if grid[i][j] == '^':
                    for offset in (-1,+1):
                        if grid[i][j+offset] == '.':
                            grid[i][j+offset] = 0
                        grid[i][j+offset] += grid[i-1][j]
                elif isinstance(grid[i][j], int):
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] = grid[i-1][j]
    timelines = 0
    for term in grid[-1]:
        if isinstance(term, int):
            timelines += term
    return timelines
    
            
def recursive_quantum_splitter(grid): ## too slow :(
    if len(grid) == 1:
        return 1
    for i in range(len(grid[0])):
        if grid[0][i] == 'S' or grid[0][i] == '|':
            if grid[1][i] == '^':
                l_timeline = deepcopy(grid)
                l_timeline[1][i-1] = '|'
                r_timeline = deepcopy(grid)
                r_timeline[1][i+1] = '|'
                return recursive_quantum_splitter(l_timeline[1:]) + recursive_quantum_splitter(r_timeline[1:])
            else:
                new_grid = deepcopy(grid)
                new_grid[1][i] = '|'
                return recursive_quantum_splitter(new_grid[1:])

def main():
    input = get_input('input.txt')
    splits = quantum_splitter(input)
    print(splits)



start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")