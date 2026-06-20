def largest_number(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

print(largest_number([3, 9, 2, 15, 7]))