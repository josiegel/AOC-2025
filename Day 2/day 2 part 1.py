def get_input(input):
    txt = []
    with open(input, 'r') as file:
        txt = file.read()
        ls = txt.split(',')
        output = []
        for item in ls:
            item = item.split('-')
            output.append((int(item[0]),int(item[1])))
    return output

def check_valid(id):
    id = str(id)
    midpoint = int(len(id) / 2)
    if id[:midpoint] == id[midpoint:]:
        return False
    else:
        return True

def main():
    ranges = get_input("input.txt")
    ans = 0
    for r in ranges:
        for id in range(r[0],r[1]+1):
            if not check_valid(id):
                ans += id
    print(ans)


main()