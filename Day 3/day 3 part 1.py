import time

def get_input(input):
    output = []
    with open(input, 'r') as file:
        for line in file:
            output.append(list(map(int, list(line.strip()))))
    return output


def get_joltage(bank):
    joltage=11
    for i in range(len(bank)-1):
        for j in range(i+1, len(bank)):
            joltage = max(joltage, (10 * bank[i]) + bank[j])
    return joltage

def main():
    banks = get_input("input.txt")
    jolts = 0
    for bank in banks:
        jolts += get_joltage(bank)
    print(jolts)


start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")