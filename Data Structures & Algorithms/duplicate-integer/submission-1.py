class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = {}
        for n in nums:
            if n in myDict:
                return myDict[n]
            else:
                myDict[n] = True
        return False