class Solution:
    def countAndSay(self, n: int) -> str: #4
        if n == 1:
            return "1"
        
        
        #recursive
        curr_n = self.countAndSay(n-1) 
        
        count = 1
        result = "" 
        
        num = curr_n[0]
        
        for i in range(1,len(curr_n)):
            if curr_n[i] == num:
                count += 1
            else:
                result += str(count)
                result += str(num)
                num = curr_n[i]
                count = 1
        
        
        result += str(count)
        result += str(num)
        
        return result
        
                