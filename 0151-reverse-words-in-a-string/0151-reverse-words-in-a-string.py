class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = s.strip().split()
        return " ".join(sentence[::-1])