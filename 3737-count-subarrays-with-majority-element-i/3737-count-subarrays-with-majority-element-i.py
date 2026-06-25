class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # Prefix sums range from -n to n, use an offset to avoid negative indices
        offset = n
        counts = [0] * (2 * n + 1)
        
        current_sum = 0
        counts[current_sum + offset] = 1  
        
        smaller = 0
        total_subarrays = 0
        
        for num in nums:
            prev_sum = current_sum
            if num == target:
                current_sum += 1
               
                smaller += counts[prev_sum + offset]
            else:
                current_sum -= 1
               
                smaller -= counts[current_sum + offset]
            
            total_subarrays += smaller
            counts[current_sum + offset] += 1
            
        return total_subarrays
