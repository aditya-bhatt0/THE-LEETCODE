from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                # Land -> Water
                land_finish = landStartTime[i] + landDuration[i]
                ans = min(
                    ans,
                    max(land_finish, waterStartTime[j]) + waterDuration[j]
                )

                # Water -> Land
                water_finish = waterStartTime[j] + waterDuration[j]
                ans = min(
                    ans,
                    max(water_finish, landStartTime[i]) + landDuration[i]
                )

        return ans