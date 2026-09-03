class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full = set(range(len(nums)+1))
        for i in full:
            if i not in nums:
                return i
        return 0
