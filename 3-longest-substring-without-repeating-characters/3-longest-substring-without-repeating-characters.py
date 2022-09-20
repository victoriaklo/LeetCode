class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        if len(s) <= 1:
            return len(s)
        
        char_dict = {}
        start = 0
        max_sub = 0
        
        for i, c in enumerate(s):
            if c in char_dict:
                start = max(start, char_dict[c] + 1)
            
            max_sub = max(max_sub, i - start + 1)
            char_dict[c] = i
        
        return max_sub
        