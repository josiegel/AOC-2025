import time
directions = ((-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1))

def get_input(input):
    output = []
    with open(input, 'r') as file:
        for line in file:
            output.append(list(line.strip()))
    return output



def check_point(point, grid, symbol='@'):
    if 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0]):
        if grid[point[0]][point[1]] == symbol:
            return True
    return False

def check_access(point, grid):
    neighbors = 0
    for d in directions:
        if check_point(move(point,d), grid):
            neighbors += 1
    if neighbors < 4:
        return True
    else:
        return False

def move(a,b):
    return(a[0] + b[0], a[1]+b[1])

def checker(grid):
    found_new = False
    rolls = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if check_point((i,j),grid) and check_access((i,j),grid):
                grid[i][j] = 'x'
                found_new = True
                rolls += 1
    if not found_new:
        return rolls
    else:
        return rolls + checker(grid)

def main():
    grid = get_input("input.txt")
    rolls = checker(grid)
    print(rolls)


start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")