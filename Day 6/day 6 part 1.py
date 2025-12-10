import time
import math

def get_input(input):
    output = []
    with open(input, 'r') as file:
        for line in file:
            output.append(line.strip().split())
    return output

def run_ops(matrix):
    total = 0
    for i in range(len(matrix[0])):
        terms = []
        for n in range(len(matrix)-1):
            terms.append(int(matrix[n][i]))
        if matrix[-1][i] == '+':
            total += sum(terms)
        if matrix[-1][i] == '*':
            total += math.prod(terms)
    return total


def main():
    input = get_input('input.txt')
    total = run_ops(input)
    print(total)
    




start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")