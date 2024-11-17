#
# @lc app=leetcode.cn id=221 lang=python3
# @lcpr version=30204
#
# [221] 最大正方形
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if dp[i][j] != 1:
                    continue
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        max_ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                max_ans = max(max_ans, dp[i][j] * dp[i][j])

        return max_ans


# @lc code=end


#
# @lcpr case=start
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0","1"],["1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

#
