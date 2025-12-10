import time
import math
NUMOFJUNCTIONS = 20

def get_input(input):
    output = []
    with open(input, 'r') as file:
        for line in file:
            output.append(list(map(int,line.strip().split(','))))
    global NUMOFJUNCTIONS 
    NUMOFJUNCTIONS = len(output)
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

def check_answer(circuits):
    for circuit in circuits:
        if len(circuit) < NUMOFJUNCTIONS:
            return False
    return True


def main():
    input = get_input('input.txt')
    distances = create_distance_matrix(input)
    circuits = []
    num_of_connections = 0
    while True:
        newest_circuit = make_circuit(distances)
        circuits.append(set(newest_circuit))
        circuits = consolidate_circuits(circuits)
        num_of_connections += 1
        print(num_of_connections," connections made!")
        if check_answer(circuits):
            print(input[newest_circuit[0]][0] * input[newest_circuit[1]][0])
            return True


start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")