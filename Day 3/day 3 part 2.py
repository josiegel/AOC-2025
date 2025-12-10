import time

def get_input(input):
    output = []
    with open(input, 'r') as file:
        for line in file:
            output.append(list(map(int, list(line.strip()))))
    return output

def convert_joltage(joltage):
    output = 0
    for i in range(len(joltage)):
        output += joltage[i] * (10 ** ((len(joltage)-1)-i))
    return output

def test_feasability(sm, lg):
    if not sm:
        return True
    for digit in lg:
        if digit == sm[0]:
            sm = sm[1:]
        if not sm:
            return True
    return False

def get_joltage(bank, digits_remaining=12):
    digits = []
    for i in range(digits_remaining):
        val = 1
        for j in range(len(bank)-(11-i)):
            if test_feasability(digits, bank[:j]):
                val = max(val, bank[j])
        digits.append(val)
    return convert_joltage(digits)

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