class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary with num as key and pair as value
        # pair = taret - num
        # if pair in dictionary, return num and pair indexes
        
        num_dict = defaultdict(int)
        
        for i, num in enumerate(nums):
            pair = target - num
            if pair in num_dict:
                return [i, num_dict[pair]]
            
            num_dict[num] = i

        