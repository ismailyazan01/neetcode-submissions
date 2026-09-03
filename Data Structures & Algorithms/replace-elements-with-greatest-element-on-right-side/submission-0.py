class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curMax = -1
        for i in range(1, len(arr) + 1):
            temp = arr[-i]
            arr[-i] = curMax
            if temp > curMax:
                curMax = temp
        if len(arr) > 0:
            arr[-1] = -1
        return arr