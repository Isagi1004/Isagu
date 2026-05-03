class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        m=[]

        for i in nums:
            count=0
            for j in nums:
                if(j!=i and j<i):
                    count+=1
            m.append(count)
            
        return m
        