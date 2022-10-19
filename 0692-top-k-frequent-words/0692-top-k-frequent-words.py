class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = defaultdict(int)
        result = []
        
        for word in words:
            word_count[word] += 1
        
        # sorts it by value
        sorted_dict = sorted(word_count.items(), key = lambda x: (-x[1], x[0]))
        
        for i in sorted_dict[:k]:
            result.append(i[0])
        
        return result