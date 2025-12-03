def get_combo(input):
    combo = []
    with open(input, 'r') as file:
        for line in file:
            code = line.strip()
            combo.append([code[:1],int(code[1:])])
    return combo

def run_command(position, command):
    if command[0] == 'R':
        position += command[1]
    if command[0] == 'L':
        position -= command[1]
    while position > 99:
        position -= 100
    while position < 0:
        position += 100
    return position

def get_password(combo, position = 50, password = 0):
    for command in combo:
        position = run_command(position, command)
        if position == 0:
            password += 1
    return password


def main():
    combo = get_combo('input.txt')
    print(get_password(combo))

main()