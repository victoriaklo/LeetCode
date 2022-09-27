class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.helper(s) == self.helper(t)
        
    
    def helper(self, str1):
        # iterate through the str
        result = []
        
        for char in str1:
            if char != "#":
                result.append(char)
            else:
                if result: result.pop()
                
        return "".join(result)