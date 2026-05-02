class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = -1
        total = 0

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
            total += num

        n = len(nums)
        expected = n * (n + 1) // 2
        missing = expected - (total - duplicate)

        return [duplicate, missing]