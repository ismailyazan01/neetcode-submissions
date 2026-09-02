class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNum = 0
        curMax = 0
        for n in nums:
            if n == 1:
                curMax += 1
            else:
                maxNum = max(curMax, maxNum)
                curMax = 0
        maxNum = max(curMax, maxNum)
        return maxNum