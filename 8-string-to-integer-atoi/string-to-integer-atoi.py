class Solution:
    def myAtoi(self, str: str) -> int:
        res=0
        a=1
        s=str.strip()
        if not s:
            return 0
        if s[0]=='-' or s[0]=='+':
            if s[0]=='-':
                a=-1
            s=s[1:]
        for i in s:
            if not i.isdigit():
                break
            res=res*10+int(i)
        res=res*a
        if res<-2**31:
            return -2**31
        elif res>2**31-1:
            return 2**31-1
        return res