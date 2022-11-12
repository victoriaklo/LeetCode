class Solution:
    def arraySign(self, nums: List[int]):

        product = 1
        for num in nums:
            product *= num
            
        if product == 0:
            return 0
        elif product < 0: 
            return -1
        else: 
            return 1
        