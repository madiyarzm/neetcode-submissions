class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()

        for i in range(len(nums)):

            if i != 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            target = -1 * nums[i]
            
            while l < r:

                if l < r and nums[l] + nums[r] < target:
                    l += 1
                
                elif l < r and nums[l] + nums[r] > target:
                    r -= 1
                
                if l < r and nums[l] + nums[r] == target:
                    result.append([target * -1, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        


        return result