class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        current = maxm = 0

        for i in nums:
            if i == 1:
                current += 1
            else: 
                if current>maxm:
                    maxm = current
                current = 0
        if current > maxm:
            maxm = current
        
        return maxm
            
            

        



        