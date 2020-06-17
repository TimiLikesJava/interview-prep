class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        i = 0
        for j in range(len(nums)):
            if(nums[j] == 0):
                count += 1
            else:
                nums[i] = nums[j]
                i += 1
        for k in range(count):
            nums[len(nums)-1-k] = 0
        return nums
