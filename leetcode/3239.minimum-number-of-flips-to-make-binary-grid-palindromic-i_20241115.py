#
# @lc app=leetcode.cn id=3239 lang=python3
# @lcpr version=30204
#
# [3239] 最少翻转次数使二进制矩阵回文 I
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 行回文
        row_res = 0
        for i in range(m):
            left, right = 0, n - 1
            while left < right:
                if grid[i][left] != grid[i][right]:
                    row_res += 1
                left, right = left + 1, right - 1
        # 列回文
        col_res = 0
        for j in range(n):
            top, bottom = 0, m - 1
            while top < bottom:
                if grid[top][j] != grid[bottom][j]:
                    col_res += 1
                top, bottom = top + 1, bottom - 1

        return min(row_res, col_res)


# @lc code=end


#
# @lcpr case=start
# [[1,0,0],[0,0,0],[0,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,1],[0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1],[0]]\n
# @lcpr case=end

#
