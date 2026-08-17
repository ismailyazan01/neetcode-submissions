class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = {}
        for i in nums:
            if i in myDict:
                return True
            else:
                myDict[i] = False
        return False