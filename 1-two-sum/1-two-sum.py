class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create an empty dict
        nums_dict = {}
        
        # create a dictionary with all values in the list as keys, and indexes as the value,
        # do this by doing ONE for loop, and call enumerate on nums
        
        for i, num in enumerate(nums):
            # create a new variable to find the diff
            diff = target - num
            
            #if the diff is in dict, return the list of indicies
            if diff in nums_dict:
                return [nums_dict[diff], i]
            
            #assign the dict key to the num and the index as value
            nums_dict[num] = i