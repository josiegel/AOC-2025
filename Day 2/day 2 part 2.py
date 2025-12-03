import time
import textwrap


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
    size = len(id)
    if size < 2:
        return True
    chunk_attempts = []
    for i in range(size-1, 0, -1):
        if not size % i:
            if not chunk_attempts:
                chunk_attempts.append(i)
            else:
                factor = False
                for test in chunk_attempts:
                    if not test % i:
                        factor = True
                if not factor:
                    chunk_attempts.append(i)
    chunk_attempts.reverse()
    #print(chunk_attempts)
    for chunk in chunk_attempts:
        checking = textwrap.wrap(id, chunk)
        if len(set(checking)) == 1:
            #print(id)
            return False
    return True

def main():
    ranges = get_input("input.txt")
    ans = 0
    for r in ranges:
        for id in range(r[0],r[1]+1):
            if not check_valid(id):
                ans += id
    print(ans)


start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")