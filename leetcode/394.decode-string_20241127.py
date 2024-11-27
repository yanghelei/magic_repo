#
# @lc app=leetcode.cn id=394 lang=python3
# @lcpr version=30204
#
# [394] 字符串解码
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        idx = 0
        while idx < len(s):
            if s[idx] != "]":
                stk.append(s[idx])
            else:
                word = []
                while stk and stk[-1] != "[":
                    word.append(stk.pop())
                stk.pop()
                cnt = []
                while stk and ord("0") <= ord(stk[-1]) <= ord("9"):
                    cnt.append(stk.pop())
                word = list(reversed(word))
                cnt = int("".join(list(reversed(cnt))))
                word = word * cnt
                stk.extend(word)
            idx += 1
        return "".join(stk)


# @lc code=end


#
# @lcpr case=start
# "3[a]2[bc]"\n
# @lcpr case=end

# @lcpr case=start
# "3[a2[c]]"\n
# @lcpr case=end

# @lcpr case=start
# "2[abc]3[cd]ef"\n
# @lcpr case=end

# @lcpr case=start
# "abc3[cd]xyz"\n
# @lcpr case=end

#
