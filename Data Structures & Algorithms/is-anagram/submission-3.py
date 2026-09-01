class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        if len(s) != len(t):
            return False
        for i in s:
            if sDict.get(i) == None:
                sDict[i] = 1
            else:
                sDict[i] += 1
        for j in t:
            if sDict.get(j) != None:
                if sDict[j] != 0:
                    sDict[j] -= 1
                else:
                    return False
            else:
                return False
        return True