def read_rotations():
    rotations = []
    with open("src/2025/day01/input.txt", "r") as file:
        for line in file.read().splitlines():
            if line.startswith("L"):
                rotations.append(- int(line[1:]))
            else:
                rotations.append(int(line[1:]))

    return rotations

def part1():
    rotations = read_rotations()
    current = 50
    password = 0

    for r in rotations:
        current = (current + r) % 100
        if current == 0:
            password += 1

    print("The password is", password % 100)

def part2():
    rotations = read_rotations()
    current = 50
    password = 0

    for r in rotations:
        old = current
        current += r
        if current < 0 and old == 0:
            current += 100
        if current == 0 or current < 0 and current % 100 == 0:
            password += 1
        password += abs(current // 100)
        current %= 100
        
        print(old, r, "->", current, "     abs:", abs((old + r) / 100))
        print("Zeroes:", password)
    
    print("The 0x434C49434B password is", password)

def main():
    part1()
    part2()


if __name__ == "__main__":
    main()