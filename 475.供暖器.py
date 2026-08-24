#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def findRadius2(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()

        def find_heaters(house: int):
            left = bisect.bisect_left(heaters, house)
            if left >= len(heaters) or left > 0 and house - heaters[left - 1] < heaters[left] - house:
                return heaters[left - 1]
            return heaters[left]

        radius = 0
        for house in houses:
            heater = find_heaters(house)
            radius = max(radius, abs(house - heater))
        return radius
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        j = 0
        houses.sort()
        heaters.sort()
        ans = 0
        for i, house in enumerate(houses):
            cur =  abs(house - heaters[j])
            while j + 1 < len(heaters) and abs(houses[i] - heaters[j]) >= abs(houses[i] - heaters[j + 1]):
                j += 1
                cur = min(cur, abs(houses[i] - heaters[j]))
            ans = max(ans, cur)
        return ans

        
# @lc code=end

