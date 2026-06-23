class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def check(s1, d1, s2, d2):
            t1 = min(s + d for s, d in zip(s1, d1))
            return min(max(t1, s) + d for s, d in zip(s2, d2))
            
        return min(
            check(landStartTime, landDuration, waterStartTime, waterDuration),
            check(waterStartTime, waterDuration, landStartTime, landDuration)
        )
