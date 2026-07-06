class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        mx = 0
        current = 1

        l = 0
        r = len(heights) - 1

        while l < r:
            current = min(heights[l], heights[r])
            mx = max(mx, current * (r - l))

            if current == heights[l]:
                l += 1

            else:
                r -= 1
        
        return mx