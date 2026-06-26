class FenwickTree:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, index: int, delta: int):
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)

    def query(self, index: int) -> int:
        sum_val = 0
        while index > 0:
            sum_val += self.tree[index]
            index -= index & (-index)
        return sum_val

class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        offset = n + 1
        bit = FenwickTree(n + offset)
        
        bit.update(0 + offset, 1)
        
        current_prefix_sum = 0
        total_subarrays = 0
        
        for num in nums:
            if num == target:
                current_prefix_sum += 1
            else:
                current_prefix_sum -= 1
                
            shifted_sum = current_prefix_sum + offset
            total_subarrays += bit.query(shifted_sum - 1)
            bit.update(shifted_sum, 1)
            
        return total_subarrays
