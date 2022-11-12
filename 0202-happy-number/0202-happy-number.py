class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sum_squares(n)
            
        if n == 1:
            return True
        
        return False
    
    def sum_squares(self, n):
        result = 0
        
        while n:
            num = n % 10
            num = num ** 2
            result += num
            n = n // 10
        
        return result
        