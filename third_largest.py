class Solution():
    def third_max(self, nums):
        

        largest = sec = third = float('-inf')

        for i in nums:
            if i == largest or i == sec or i == third:
                continue
            
            if i > largest:
                third = sec
                sec = largest
                largest = i
            elif i > sec:
                third = sec
                sec = i
            elif i > third:
                third = i

        return third if third != float('-inf') else largest

clean = input().strip("[]").replace(","," ")
nums = list(map(int, clean.split()))
print(Solution().third_max(nums))