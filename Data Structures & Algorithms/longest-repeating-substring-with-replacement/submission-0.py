from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mx = 0
        freq = defaultdict(int) #stores frequency counter for each element

        for r in range(len(s)):
            freq[s[r]] += 1 

            while (r - l + 1) - max(freq.values()) > k:   #we find majoirty element, and if there are more minority than allowed, shrink window
                freq[s[l]] -= 1
                l += 1
            
            mx = max(mx, r - l + 1) #update after

        return mx
            
            
        