class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        for i in operations:
            match(i):
                case'+':
                    op1=s[-1]
                    op2=s[-2]
                    s.append(op1+op2)
                case 'D':
                    op=s[-1]
                    s.append(op*2)
                case'C':
                    s.pop()
                case _:
                    s.append(int(i))
        sum1=0
        if s:
            sum1=sum(s)
        return sum1
