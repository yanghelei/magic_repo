#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30204
#
# [121] 买卖股票的最佳时机
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        max_profit = 0
        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return max_profit


# @lc code=end


#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#