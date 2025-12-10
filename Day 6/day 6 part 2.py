import time
import math

def get_input(input):
    output = []
    with open(input, 'r') as file:
        for line in file:
            output.append(line.strip('\n'))
    return output

def run_cephalopod_ops(matrix):
    total = 0
    ops = matrix[-1]
    digits = matrix[:-1]
    op_positions = []
    for i in range(len(ops)):
        if ops[i] != ' ':
            op_positions.append(i)
    op_positions.append(max(len(row) for row in matrix)+1)
    for i in range(len(op_positions)-1):
        terms = []
        num_terms = op_positions[i+1] - op_positions[i] - 1
        for j in range(num_terms):
            term = ''
            for row in digits:
                term = term + row[op_positions[i]+j]
            terms.append(int(term))
        if ops[op_positions[i]] == '+':
            total += sum(terms)
        if ops[op_positions[i]] == '*':
            total += math.prod(terms)
    return total


def main():
    input = get_input('input.txt')
    total = run_cephalopod_ops(input)
    print(total)



start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")