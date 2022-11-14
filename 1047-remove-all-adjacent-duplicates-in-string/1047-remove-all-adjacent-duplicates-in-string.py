class Solution:
    def removeDuplicates(self, s: str) -> str:
        # while loop to iterate through 
        
        result = []
        
        for char in s:
            if result and char == result[-1]:
                result.pop()
            else:
                result.append(char)
            
        
        return "".join(result)