class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=list()
        sum=0
        if len(nums)>=1 and len(nums)<=1000:
            for i in nums:
                if i>=-10**6 and i<=10**6:
                    sum+=i
                    l.append(sum)
        return l