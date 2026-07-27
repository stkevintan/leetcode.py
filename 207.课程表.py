#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        for item in prerequisites:
            edges[item[1]].append(item[0])
        visited = [0] * numCourses
        ans = True
        def dfs(u):
            nonlocal ans
            if ans == False: return
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 1:
                    # loop
                    ans = False
                    return
                if visited[v] == 0:
                    dfs(v)
            visited[u] = 2
        for i in range(numCourses):
            if not ans: return False
            if visited[i] == 0:
                dfs(i)
        return ans


        
# @lc code=end

