
def parse_input(file_contents: list[str]):
    left_list = []
    right_list = []
    for line in file_contents:
        left_number, right_number = line.split("   ")
        left_list.append(int(left_number))
        right_list.append(int(right_number))

    return left_list, right_list

def quicksort(nums: list[int], low: int=0, high: int=None) -> list[int]:
    if high == None:
        high = len(nums) - 1
    
    if (low < high):
        pivot_location = partition(nums, low, high)
        quicksort(nums, low, pivot_location - 1)
        quicksort(nums, pivot_location + 1, high)

def partition(nums: list[int], low: int, high: int) -> int:
    i = low - 1

    for j in range(low, high):
        if nums[j] < nums[high]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    i += 1
    nums[i], nums[high] = nums[high], nums[i]

    return i

def find_total_distance(left: list[int], right: list[int]):
    return sum([abs(left[i] - right[i]) for i in range(len(left))])

def find_similarity_score(left: list[int], right: list[int]):
    return sum([number * right.count(number) for number in left])

def main():
    with open("inputs/day01.txt", "r") as file:
        contents = file.readlines()
    
    #left_list, right_list = parse_input(contents)
    left_list, right_list = [1,2,6,8,5], [5,5,8,1,3]
    quicksort(left_list, 0, len(left_list) - 1)
    quicksort(right_list, 0, len(right_list) - 1)

    distance = find_total_distance(left_list, right_list)

    similarity_score = find_similarity_score(left_list, right_list)
    print(similarity_score)
    

if __name__ == "__main__":
    main()