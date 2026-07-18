import math

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        # Find the smallest and largest numbers in the array
        min_val = min(nums)
        max_val = max(nums)
        
        # Return their Greatest Common Divisor
        return math.gcd(min_val, max_val)
