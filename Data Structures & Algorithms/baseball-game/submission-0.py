class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for s in operations:
            if s == '+':
                res = int(stack[-2]) + int(stack[-1])
                stack.append(res)
                continue
            if s == 'C':
                stack.pop()
                continue
            if s == 'D':
                res = int(stack[-1]) * 2
                stack.append(res) 
                continue

            stack.append(s)
            

        num = 0
        for i in stack:
            num += int(i)
        
        return num