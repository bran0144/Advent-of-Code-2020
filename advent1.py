

# test_list = [1721, 979, 366, 299, 675, 1456]

with open("numbers.txt") as file:
    nums = [int(line.strip()) for line in file]
    set_nums = set(nums)


def add_to_2020(nums, set_nums):
    for num in nums:
        if 2020 - num in set_nums:
            return(num * (2020 - num))

print(add_to_2020(nums, set_nums))


def three_to_2020(nums, set_nums):
    for num1 in nums:
        for num2 in nums:
            if (2020 - num1 - num2) in set_nums:
                return (num1 * num2 * (2020 - num1 - num2))

print(three_to_2020(nums, set_nums))
