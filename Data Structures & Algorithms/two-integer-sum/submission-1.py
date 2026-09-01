class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        right = 0
        left = 1
        while right < len(nums):
            if nums[right] + nums[left] == target:
                return [right, left]
            else:
                if left == len(nums) - 1:
                    right += 1
                    left = right + 1
                else:
                    left += 1

        