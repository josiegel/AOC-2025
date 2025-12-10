import time
import math

def get_input(input):
    output = []
    with open(input, 'r') as file:
        for line in file:
            output.append(list(map(int,line.strip().split(','))))
    return output

def get_distance(pointa, pointb):
    if pointa == pointb:
        return 0
    else:
        return math.sqrt(((pointa[0] - pointb[0]) ** 2) + ((pointa[1] - pointb[1]) ** 2) + ((pointa[2] - pointb[2]) ** 2))

def create_distance_matrix(points):
    distance_matrix = []
    for i in range(len(points)):
        distance_matrix.append([])
    for row in distance_matrix:
        for i in range(len(points)):
            row.append([])
    for i in range(len(points)):
        for j in range(len(points)):
            distance_matrix[i][j] = get_distance(points[i],points[j])
    return distance_matrix

def make_circuit(distances):
    pointa = 0
    pointb = 0
    shortest = math.inf
    for a in range(len(distances)):
        for b in range(len(distances)):
            if 0 < distances[a][b] < shortest:
                shortest = distances[a][b]
                pointa = a
                pointb = b
    distances[pointa][pointb] = 0
    distances[pointb][pointa] = 0
    return (pointa, pointb)

def consolidate_circuits(circuits):
    circuit_sets = list(map(set,circuits))
    new_circuits = []
    while len(circuit_sets) > 0:
        i = 1
        while i < len(circuit_sets):
            if circuit_sets[0] & circuit_sets[i]:
                circuit_sets[0] = circuit_sets[0] | circuit_sets[i]
                circuit_sets.pop(i)
                i = 0
            i += 1
        new_circuits.append(circuit_sets.pop(0))
    return(new_circuits)

def get_answer(circuits):
    lengths = []
    for circuit in circuits:
        lengths.append(len(circuit))
    lengths.sort(reverse=True)
    return (lengths[0] * lengths[1] * lengths[2])


def main():
    input = get_input('input.txt')
    distances = create_distance_matrix(input)
    circuits = []
    for i in range(1000):
        print(1000-i, " circuits remaining!")
        circuits.append(make_circuit(distances))
    circuits = consolidate_circuits(circuits)
    answer = get_answer(circuits)
    print(answer)


start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")