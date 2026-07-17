from collections import Counter
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            c = 0
            for x in range(g, mx + 1, g):
                c += freq[x]
            cnt[g] = c * (c - 1) // 2

        exact = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            exact[g] = cnt[g]
            for x in range(g * 2, mx + 1, g):
                exact[g] -= exact[x]

        pref = []
        vals = []
        s = 0
        for g in range(1, mx + 1):
            if exact[g]:
                s += exact[g]
                vals.append(g)
                pref.append(s)

        return [vals[bisect_right(pref, q)] for q in queries]