class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:
            try:
                record.append(int(i))
            except ValueError:
                if i == "+":
                    record.append(record[-1] + record[-2])
                elif i == "D":
                    record.append(record[-1] * 2)
                else:
                    record.pop()
        sums = 0
        for i in record:
            sums += i
        return sums