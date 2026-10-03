class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        max_val = max(nums)
        min_val = min(nums)
        diff = (max_val-k) - (min_val+k)
        return max(0, diff)
