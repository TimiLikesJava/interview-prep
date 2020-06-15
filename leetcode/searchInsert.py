class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        if nums.count(target)>0: return nums.index(target)
        return len([x for x in nums if x < target])
