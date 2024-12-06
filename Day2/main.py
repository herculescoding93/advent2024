file = open("input.txt", "r")

sets = []

for i in file.readlines():
    sets.append(list(map(int, i.split())))

def meets_criteria(nums):
    # Check for differences between adjacent numbers
    differences = [abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1)]
    if not all(1 <= diff <= 3 for diff in differences):
        return False
    # Check for consistent increasing or decreasing order
    is_increasing = all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))
    is_decreasing = all(nums[i] > nums[i + 1] for i in range(len(nums) - 1))
    return is_increasing or is_decreasing

safe = 0


for set in sets:
    if meets_criteria(set):
        safe+=1
        continue

    for i in range(len(set)):
        modList = set[:i] + set[i + 1:]
        print(modList)
        if meets_criteria(modList):
            safe+=1
            break

print(safe)
