class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        mx = 0

        heights.append(0)

        for i in range(len(heights)):

            start_index = i

            while stack and stack[-1][1] > heights[i]:
                index, h = stack.pop()
                mx = max(mx, (i - index) * h)
                
                start_index = index
            
            stack.append((start_index, heights[i]))
        
        
        return mx
