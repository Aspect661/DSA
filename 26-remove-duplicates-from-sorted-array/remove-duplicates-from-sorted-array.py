class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i, j = 0, 1
        count = 1
        n = len(nums)
        while j < n:
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                count += 1

        return count


        
        



            
