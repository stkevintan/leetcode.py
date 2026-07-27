#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1; right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
                
                while left < right and right + 1 < len(nums) and nums[right + 1] == nums[right]:
                    right-=1
                while left < right and left - 1 > i and nums[left - 1] == nums[left]:
                    left+=1
        return ans

# @lc code=end

