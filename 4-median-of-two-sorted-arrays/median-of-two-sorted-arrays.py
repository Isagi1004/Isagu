class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        if(len(nums3)==1):
            return nums3[len(nums3)-1]
        elif(len(nums3)%2!=0):
            a=(len(nums3)-1)/2
            return nums3[int(a)]
        else:
            a=len(nums3)/2
            b=a+0.5
            c=a-0.5
            return (nums3[int(b)]+nums3[int(c)])/2