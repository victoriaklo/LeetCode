class Solution:
    def hammingWeight(self, n: int) -> int:
        # ans=0
        # while(n):
        #     ans+=(n%2)
        #     n=n//2
        # return(ans)
        
        return bin(n).count("1")