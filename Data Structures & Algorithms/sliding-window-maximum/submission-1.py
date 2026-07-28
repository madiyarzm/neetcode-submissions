import heapq
#from collections import defaultdict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []

        l = 0
        #active = defaultdict(bool)

        for r in range(len(nums)):
            heapq.heappush(heap, (nums[r] * -1, r))
            #active[r] = True
            
            if (r - l + 1) > k:
                #active[l] = False
                l += 1

            while heap:

                item, item_id = heap[0]

                if item_id < l:
                    heapq.heappop(heap)
                    continue
                
                else:
                    if (r - l + 1) == k:
                        result.append(item * -1)

                    break


        return result