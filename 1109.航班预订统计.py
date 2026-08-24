#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] * n
        for booking in bookings:
            start, end, value = booking[0] - 1, booking[1] - 1, booking[2]
            seats[start] += value
            if end + 1 < n:
                seats[end + 1] -= value
        for i in range(1, n):
            seats[i] += seats[i - 1]
        return seats
        
# @lc code=end

