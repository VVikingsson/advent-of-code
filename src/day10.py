def find_trails(map, i, j):
    current = map[i][j]
    total = set()
    part2 = 0
    
    if current == 9:
        total.add((i, j))
        part2 += 1

    if i > 0 and map[i-1][j] == current + 1:
        findings = find_trails(map, i-1, j)
        total.update(findings[0])
        part2 += findings[1]

    if i + 1 < len(map) and map[i+1][j] == current + 1:
        findings = find_trails(map, i+1, j)
        total.update(findings[0])
        part2 += findings[1]

    if j > 0 and map[i][j-1] == current + 1:
        findings = find_trails(map, i, j-1)
        total.update(findings[0])
        part2 += findings[1]

    if j + 1 < len(map[i]) and map[i][j+1] == current + 1:
        findings = find_trails(map, i, j+1)
        total.update(findings[0])
        part2 += findings[1]

    if current == 0:
        print(i, j, "found", len(total), "hilltops at:")
        return len(total), part2
    return total, part2

def main():
    with open("inputs/day10.txt", "r") as file:
        contents = file.readlines()

    hilltops = 0
    trails = 0
    map = [[int(num) for num in row.strip()] for row in contents]

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                findings = find_trails(map, i, j)
                hilltops += findings[0]
                trails += findings[1]

    print(hilltops, trails)

if __name__ == "__main__":
    main()