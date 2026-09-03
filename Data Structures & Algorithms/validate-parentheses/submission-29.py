class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myDict = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            print(i)
            print(0)
            print(myDict.get(i))
            print(1)
            print(stack)
            if myDict.get(i) != None:
                print(2)
                stack.append(myDict.get(i))
                print(stack)
            elif len(stack) == 0:
                return False
            elif stack.pop() != i:
                return False
        if len(stack) > 0:
            return False
        return True