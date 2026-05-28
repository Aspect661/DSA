class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        def square(nums):
            result = [i**2 for i in nums]
            return result

        squared_nums = square(nums)

        squared_nums.sort()

        return squared_nums