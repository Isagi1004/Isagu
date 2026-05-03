class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        m=[]
        count=0
        for i in nums:
            for j in nums:
                if(j!=i and j<i):
                    count+=1
            m.append(count)
            count=0
        return m
        