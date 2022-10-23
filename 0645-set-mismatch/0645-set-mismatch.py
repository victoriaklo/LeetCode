class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        num_to_remove = sum(nums) - sum(set(nums))
        missing = sum(range(1, len(nums) +1)) - sum(set(nums))
        
        return [num_to_remove, missing]
                