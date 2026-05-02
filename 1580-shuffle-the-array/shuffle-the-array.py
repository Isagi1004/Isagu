class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=[]
        b=[]
        m=[]
        for i in range(0,n):
            a.append(nums[i])
        for j in range(n,len(nums)):
            b.append(nums[j])
        for k in range(n):
            
            m.append(a[k])
            m.append(b[k])
        return m
        