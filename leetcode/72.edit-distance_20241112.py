#
# @lc app=leetcode.cn id=72 lang=python3
# @lcpr version=30204
#
# [72] 编辑距离
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        dp = [[0 for j in range(n2 + 1)] for i in range(n1 + 1)]

        for row in range(n1 + 1):
            dp[row][0] = row
        for col in range(n2 + 1):
            dp[0][col] = col

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                right_finished = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else dp[i - 1][j - 1] + 1
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, right_finished)

        return dp[-1][-1]


# @lc code=end


#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "intention"\n"execution"\n
# @lcpr case=end

#