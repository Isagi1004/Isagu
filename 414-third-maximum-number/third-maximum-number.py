class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        res=[]
        n=len(nums)
        if n>-1 and n<=10**4:
            for i in nums:
                if i not in res:
                    if i>=-2**31-1 and i<2**31:
                        res.append(i)
        res.sort()
        b=len(res)
        if len(res)>=3:
            return res[b-3]
        else:
            return res[len(res)-1]