def get_combo(input):
    combo = []
    with open(input, 'r') as file:
        for line in file:
            code = line.strip()
            combo.append([code[:1],int(code[1:])])
    return combo

def run_command(position, command, zeroes = 0):
    if command[0] == 'R':
        direction = 1
    if command[0] == 'L':
        direction = -1
    ticks = command[1]
    for i in range(ticks):
        position += direction
        if position < 0:
            position = 99
        if position > 99:
            position = 0
        if position == 0:
            zeroes += 1
    return position, zeroes


def get_password(combo):
    position = 50
    password = 0
    for command in combo:
        position, password = run_command(position, command, password)
    return password


def main():
    combo = get_combo('input.txt')
    print(get_password(combo))

main()