class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if nums[-1] < target:
                return len(nums)
            else:
                for num in nums:
                    if num > target:
                        return nums.index(num)