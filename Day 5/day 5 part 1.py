import time

def get_input(input):
    output = []
    with open(input, 'r') as file:
        for line in file:
            output.append(line.strip())
    ranges = output[:output.index('')]
    id_ranges = []
    for i in ranges:
        id_ranges.append(
            (int(i[:i.index('-')]),int(i[i.index('-')+1:])))
    ingredients = list(map(int,output[output.index('')+1:]))
    return (id_ranges, ingredients)

def test_ingredient(ingredient,ranges):
    for range in ranges:
        if range[0] <= ingredient <= range[1]:
            return True
    return False

def main():
    ranges, ingredients = get_input("input.txt")
    total = 0
    for ingredient in ingredients:
        if test_ingredient(ingredient,ranges):
            total += 1
    print(total)




start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")