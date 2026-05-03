class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #a=list(range(1,max(nums)+1))
        m=[]
        n=len(nums)
        arr_set = set(nums)

        for i in range(1, n + 1):
            if i not in arr_set:
                m.append(i)
        return m
        