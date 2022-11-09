class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()  # Makes it easier to pick values
        max_perimeter = 0
        
        for i in range(2, len(nums)):
            '''Sum of two sides of a triangle with non-zero area
            is always greater than the third side'''
            if nums[i - 2] + nums[i - 1] <= nums[i]:
                continue
            else:
                max_perimeter  = max(max_perimeter, sum(nums[i - 2:i + 1]))
        
        return max_perimeter