class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x>-100 and x<100 and n>=-2**31 and n<=2**31-1:
            a=pow(x,n)
        if a>=-10**4 and a<=10**4:
            return a

        