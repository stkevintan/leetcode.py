#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from collections import deque
import heapq
from typing import List

class Solution:
    # RMQ
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        bit, exp = 0, 1
        while exp < k:
            bit += 1
            exp <<= 1

        fmax = [[v if i == 0 else 0 for v in nums] for i in range(bit)]
    
        for b in range(1, bit):
            for i in range(0, len(nums) - (1 << b) + 1):
                fmax[b][i] = max(fmax[b - 1][i], fmax[b - 1][i + (1 << (b - 1))])

        b = bit - 1
        return [max(fmax[b][i], fmax[b][i + k - (1 << b)]) for i in range(len(nums) - k + 1)]

    # priority queue
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        h = [(-nums[i], i) for i in range(k)]
        heapq.heapify(h)

        ans = [-h[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(h, (-nums[i], i))
            # 去掉不符合max
            while h[0][1] <= i - k:
                heapq.heappop(h)
            ans.append(-h[0][0])
        return ans
    
    # 单调队列
    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        ans.append(nums[q[0]])
        for i in range(k, len(nums)):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        return ans
    # Sparse table
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix, suffix = [0] * n, [0] * n
        for i in range(0, n):
            if i % k == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = max(prefix[i - 1], nums[i])
        
        for i in range(n - 1, -1, -1):
            if i == n - 1 or i % k == 0:
                suffix[i] = nums[i]
            else:
                suffix[i] = max(suffix[i + 1], nums[i])
        return [max(suffix[i], prefix[i + k - 1]) for i in range(n - k + 1)]

# @lc code=end

