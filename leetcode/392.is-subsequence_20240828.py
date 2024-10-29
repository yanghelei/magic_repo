#
# @lc app=leetcode.cn id=392 lang=python3
# @lcpr version=30204
#
# [392] 判断子序列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        match_idx = 0
        for search_idx in range(len(t)):
            if s[match_idx] == t[search_idx]:
                match_idx += 1
            if match_idx == len(s):
                return True
        return match_idx == len(s)


# @lc code=end


#
# @lcpr case=start
# "abc"\n"ahbgdc"\n
# @lcpr case=end

# @lcpr case=start
# "axc"\n"ahbgdc"\n
# @lcpr case=end

#
