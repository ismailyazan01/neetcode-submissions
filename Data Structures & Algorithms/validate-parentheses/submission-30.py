class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myDict = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if myDict.get(i) != None:
                print(2)
                stack.append(myDict.get(i))
            elif len(stack) == 0:
                return False
            elif stack.pop() != i:
                return False
        if len(stack) > 0:
            return False
        return True