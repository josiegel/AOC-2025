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
            [int(i[:i.index('-')]),int(i[i.index('-')+1:])])
    return (id_ranges)

def test_ingredient(ingredient,ranges):
    for range in ranges:
        if range[0] <= ingredient <= range[1]:
            return True
    return False

def get_bounds(ranges):
    mini = ranges[0][0]
    maxi = ranges[0][1]
    for range in ranges:
        mini = min(mini, range[0])
        maxi = max(maxi, range[1])
    return mini, maxi

def consolidate_ranges(ranges):
    changes_made = False
    new_ranges = []
    for old in ranges:
        overlapping = False
        for i in range(len(new_ranges)):
            if new_ranges[i][0]-1 <= old[0] <= new_ranges[i][1]+1 or new_ranges[i][0]-1 <= old[1] <= new_ranges[i][1]+1 or old[0]-1 <= new_ranges[i][0] <= old[1]+1 or old[0]-1 <= new_ranges[i][1] <= old[1]+1:
                new_ranges[i] = [min(old[0],new_ranges[i][0]), max(old[1], new_ranges[i][1])]
                overlapping = True
                changes_made = True
        if not overlapping:
            new_ranges.append(old)
    if changes_made:
        return consolidate_ranges(new_ranges)
    else:
        new_ranges.sort(key=first_value)
        for r in new_ranges:
            print(r)
        return new_ranges

def first_value(range):
    return range[0]

def count_ingredients(ranges):
    total = 0
    for range in ranges:
        total += (range[1] + 1 - range[0])
    return total

def main():
    ranges = get_input("input.txt")
    ranges = consolidate_ranges(ranges)
    total = count_ingredients(ranges)
    print(total)
    




start_time = time.time()    
main()
end_time = time.time()
print(end_time - start_time, " seconds")