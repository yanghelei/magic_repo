#
# @lc app=leetcode.cn id=122 lang=python3
# @lcpr version=30204
#
# [122] 买卖股票的最佳时机 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for idx in range(1, len(prices)):
            diff = prices[idx] - prices[idx - 1]
            profit = profit + diff if diff > 0 else profit
        return profit
# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#
