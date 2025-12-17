class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=[]
        pr=1
        sub=0
        if n>=1 and n<=10**5:
            for i in str(n):
                a.append(int(i))
            for i in a:
                pr*=i
            for i in a:
                sub+=i
        return pr-sub

        