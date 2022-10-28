class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        # create word dict where values will be all anagrams words in str
        # key will be a list of letter in each word
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in word_dict:
                word_dict[sorted_word].append(word) 
            else:
                word_dict[sorted_word] = [word]
        
        return word_dict.values()