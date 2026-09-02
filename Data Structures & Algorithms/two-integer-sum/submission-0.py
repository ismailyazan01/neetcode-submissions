class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i in range(len(nums)):
            if myDict.get(nums[i]):
                myDict[nums[i]].append(i)
            else:
                myDict[nums[i]] = [i]

        for j in myDict:
            if myDict.get(target - j) and len(myDict[j]) == 2:
                return [myDict[j][0], myDict[j][1]]
            elif myDict.get(target - j) and target - j != j:
                return [myDict[j][0], myDict[target - j][0]]