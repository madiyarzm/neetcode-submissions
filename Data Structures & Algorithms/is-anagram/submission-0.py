class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}

        #maintaining frequency stored in hashmap
        for letter in s:
            if letter not in freq_s:
                freq_s[letter] = 1
            
            else:
                freq_s[letter] += 1
        
        for letter in t:
            if letter not in freq_t:
                freq_t[letter] = 1
            
            else:
                freq_t[letter] += 1
        
        return freq_s == freq_t

        

        