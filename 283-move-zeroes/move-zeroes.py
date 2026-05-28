class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        n = len(nums)

        i = 0
        j = 1
        while i < n-1 and j < n:
            if nums[i] == 0:
                if nums[j] == 0:
                    j += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j = i+1  
            else:
                i += 1
                j = i+1
                
            

        