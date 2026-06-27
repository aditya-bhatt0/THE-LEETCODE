from collections import Counter

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        count = Counter(nums)
        ans = 0
        
        if 1 in count:
            ans = count[1] if count[1] % 2 != 0 else count[1] - 1
            
        for x in count:
            if x == 1:
                continue
                
            current_len = 0
            curr = x
            
            while curr in count:
                if count[curr] >= 2:
                    current_len += 2
                    curr = curr * curr
                else:
                    current_len += 1
                    break
            else:
                current_len -= 1
                
            ans = max(ans, current_len)
            
        return ans
