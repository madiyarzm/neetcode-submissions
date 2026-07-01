class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        #built a decoded version -> cat -> 3#cat
        for word in strs:
            s += f"{len(word)}#{word}"
        
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = s.index("#", i) #finds index of delimeter, after i
            l = int(s[i:j]) #extracts length (12 or 3)
            res.append(s[j + 1 : j + l + 1]) #slices 
            i = j + l + 1 #advances i to next numbers
        
        return res