def parse_input():
    with open("src/2025/day05/input.txt", "r") as file:
        ranges, ids = [data.split("\n") for data in file.read().split("\n\n")]
        return ranges, ids
        
def find_fresh_ids(ranges):
    ids = set()

    for r in ranges:
        start, end = [int(id) for id in r.split("-")]
        for id in range(start, end+1):
            ids.add(id)

    return ids

def part1():
    ranges, ids = parse_input()
    count = 0

    for id in ids:
        for r in ranges:
            start, end = [int(id) for id in r.split("-")]
            if int(id) in range(start, end+1):
                count += 1
                break
    


    print("Fresh ids:", count)

def part2():
    ranges, ids = parse_input()
    ranges = [[int(n) for n in r.split("-")] for r in ranges]
    ranges.sort()
    

    print(ranges)
    combined_ranges = combine_ranges(ranges)
    print(combined_ranges)

    count = 0
    for r in combined_ranges:
        count += r[1] - r[0] + 1

    print("Part 2 ids:", count)

# Takes a sorted list of ranges and combines them as much as possible recursively
def combine_ranges(ranges: list[list[int]]):
    if len(ranges) < 2:
        return ranges
    
    if ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]:
        ranges = ranges[:1] + ranges[2:]
        return combine_ranges(ranges)

    elif ranges[1][0] - 1 <= ranges[0][1] and ranges[1][1] >= ranges[0][1]:
        ranges[0][1] = ranges[1][1]
        ranges = ranges[:1] + ranges[2:]
        return combine_ranges(ranges)
    
    else:
        return ranges[:1] + combine_ranges(ranges[1:])

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()