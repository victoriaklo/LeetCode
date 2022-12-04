from collections import Counter 

class Solution:
    def frequencySort(self, s: str) -> str:
        result = ''
        l = sorted(list(set(s)), key=s.count, reverse=True)
        for i in l:
            result += i * s.count(i)
        return result