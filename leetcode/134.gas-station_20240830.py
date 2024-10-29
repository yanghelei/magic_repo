#
# @lc app=leetcode.cn id=134 lang=python3
# @lcpr version=30204
#
# [134] 加油站
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        cur_gas = 0
        min_gas, min_idx = float("inf"), 0
        for i in range(n):
            cur_gas += gas[i] - cost[i]
            if cur_gas < min_gas:
                min_idx = i
                min_gas = cur_gas
        if cur_gas < 0:
            return -1
        else:
            return (min_idx + 1) % n


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n[3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n[3,4,3]\n
# @lcpr case=end

#
