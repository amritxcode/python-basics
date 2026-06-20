def secondlargest_number(nums):
    largest = nums[0]
    sec_largest= float('-inf')
    for num in nums:
        if num > largest:
            sec_largest = largest
            largest = num
        elif num < largest and num > sec_largest:
            sec_largest = num

    return sec_largest 

print(secondlargest_number([3, 9, 2, 15, 7]))