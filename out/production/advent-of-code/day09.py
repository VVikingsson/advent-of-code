with open("inputs/day09.txt", "r") as file:
    disk = file.read()

def checksum(files):
    checksum = 0
    
    for i in range(len(files)):
        if files[i] != ".":
            checksum += i * int(files[i])

    return checksum

def part1():
    # Format files
    files = []
    dots = 0

    for i in range(len(disk)):
        if i % 2 == 0:
            for j in range(int(disk[i])):
                files.append(i // 2)
        else:
            for j in range(int(disk[i])):
                files.append(".")
            dots += int(disk[i])   


    # Move files
    j = 0
    length = len(files)

    for i in range(length - 1, length - dots - 1, -1):
        if files[i] == ".":
            continue
        while files[j] != ".":
            j += 1
        
        files[i], files[j] = files[j], files[i]

    # Find checksum
    return checksum(files)

def part2():
    # Format files
    files = []

    for i in range(len(disk)):
        if i % 2 == 0:
            files.append(int(disk[i]) * [str(i // 2)])
        elif disk[i] != "0":
            files.append(int(disk[i]) * ".")
        
    
    # Move files
    i = len(files) - 1

    while i > 0:
        if "." in files[i]:
            pass
        else:
            j = 1
            swapped = False

            while not swapped and j < i:
                if "." in files[j]:
                    f_length = len(files[i])
                    e_length = len(files[j])

                    if e_length >= f_length:

                        if e_length > f_length:
                            left = files[j][:f_length]
                            right = files[j][f_length:]
                            files.pop(j)
                            files.insert(j, right)
                            files.insert(j, left)
                            i += 1

                        files[i], files[j] = files[j], files[i]
                        swapped = True
                        
                j += 1

        i -= 1

    result = []
    for s in files:
        for e in s:
            result.append(e)


    return checksum(result)
    
print(part1())
print(part2())
