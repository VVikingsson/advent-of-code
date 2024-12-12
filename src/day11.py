from collections import defaultdict
from copy import deepcopy

with open("inputs/day11.txt", "r") as file:
    data = [int(n) for n in file.read().split()]

stones = defaultdict(int)
for number in data:
    stones[number] = 1

print(stones)
for blink in range(75):
    if blink == 25:
        print(sum(stones.values()))
    new_stones = deepcopy(stones)
    for stone, count in stones.items():
        
        # If the stone is engraved with the number 0, 
        # it is replaced by a stone engraved with the number 1
        if stone == 0:
            new_stones[stone] -= count
            new_stones[1] += count
        
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            new_stones[stone] -= count
            left = int(str(stone)[:half])
            right = int(str(stone)[half:])

            new_stones[left] += count
            new_stones[right] += count
        
        else:
            new_stones[stone] -= count
            new_stones[stone * 2024] += count  
        
        if new_stones[stone] == 0:
            new_stones.pop(stone)

    #print("NEW\n", new_stones)

    stones = new_stones 

print(sum(stones.values()))