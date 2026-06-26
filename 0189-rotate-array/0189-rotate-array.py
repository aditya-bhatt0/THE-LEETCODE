class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]
