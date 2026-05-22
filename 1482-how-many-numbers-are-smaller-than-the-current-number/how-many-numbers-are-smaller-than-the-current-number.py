class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        n = len(nums)
        count = [0]*n
        k = 0
        for i in nums:
            for j in nums:
                if i>j:
                    count[k]+=1
            k += 1
        return count
        