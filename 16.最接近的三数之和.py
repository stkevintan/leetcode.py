#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        delta = 10 ** 9
        def select(sum: int):
            nonlocal delta
            d = sum - target
            if abs(d) < abs(delta):
                delta = d
        
        for i, a in enumerate(nums[:-2]):
            if i > 0 and a == nums[i - 1]:
                continue
            # cut 1
            cur_min = a + nums[i + 1] + nums[i + 2]
            if cur_min > target:
                select(cur_min)
                break
            # cut 2
            cur_max = a + nums[len(nums) - 1] + nums[len(nums) - 2]
            if cur_max < target:
                select(cur_max)
                continue
        
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = a + nums[l] + nums[r]
                if sum < target:
                    select(sum)
                    l += 1
                elif sum > target:
                    select(sum)
                    r -= 1
                else:
                    return target
        return target + delta
        
# @lc code=end

