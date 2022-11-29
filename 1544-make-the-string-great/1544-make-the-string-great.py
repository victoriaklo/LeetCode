class Solution:
    def makeGood(self, s: str) -> str:

        
        i = 0
        
        while i < len(s) - 1:
            if s[i] == s[i+1]:
                i+= 1
            
            elif s[i].upper() == s[i+1] or s[i] == s[i+1].upper():
                s = s[:i] + s[i+2:]
                i = 0
            else:
                i+=1
        
        return s
            

            
#         n = len(s)
#         i=0
        
#         while i < n - 1:
#             if s[i] == s[i+1].swapcase():
#                 s = s[:i] + s[i+2:]
#                 i = i - 1 if i != 0 else 0
#                 n = len(s)
#             else:
#                 i+=1
        
#         return s