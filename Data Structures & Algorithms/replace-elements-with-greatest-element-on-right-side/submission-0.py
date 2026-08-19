class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

        for i in range(len(arr)):
            mx = max(arr[i:])
            arr[i] = mx
        
        arr.append(-1)
        return arr[1:]