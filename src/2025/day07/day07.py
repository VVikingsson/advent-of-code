def parse_input():
    with open("src/2025/day07/input.txt", "r") as file:
        rows = file.read().splitlines()
        for i in range(len(rows[0])):
            if rows[0][i] == "S":
                start = i

        return rows[1:], start
    
def part1and2():
    rows, start = parse_input()
    beams = set([start])
    add = set()
    remove = set()
    splits = 0
    timelines_per_col = [1 if i == start else 0 for i  in range(len(rows[0]))]

    for row in rows:
        # Iterate only over what's necessary, thanks sets.
        for i in beams:
            if row[i] == "^":
                add.add(i-1)
                add.add(i+1)
                remove.add(i)
                splits += 1
                timelines_per_col[i-1] += timelines_per_col[i]
                timelines_per_col[i+1] += timelines_per_col[i]
                timelines_per_col[i] = 0


        beams = beams.union(add)
        beams = beams.difference(remove)
        add = set()
        remove = set()

    print("Splits:", splits)
    print("Timelines:", sum(timelines_per_col))

def main():
    part1and2()

if __name__ == "__main__":
    main()