#
# @lc app=leetcode.cn id=242 lang=python3
# @lcpr version=30204
#
# [242] 有效的字母异位词
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1
        for i in range(len(t)):
            if t[i] not in hashmap or hashmap[t[i]] == 0:
                return False
            hashmap[t[i]] -= 1
        return True


# @lc code=end


#
# @lcpr case=start
# "anagram"\n"nagaram"\n
# @lcpr case=end

# @lcpr case=start
# "rat"\n"car"\n
# @lcpr case=end

#