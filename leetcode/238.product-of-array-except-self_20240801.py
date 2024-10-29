#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30204
#
# [238] 除自身以外数组的乘积
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l2r = [1 for _ in range(len(nums))]  # 记录 idx 左侧元素的乘积
        r2l = [1 for _ in range(len(nums))]  # 记录 idx 右侧元素的乘积

        for idx in range(len(nums)):
            if idx == 0:
                continue
            l2r[idx] = l2r[idx-1] * nums[idx-1]
        for idx in reversed(range(len(nums))):
            if idx == len(nums) - 1:
                continue
            r2l[idx] = r2l[idx+1] * nums[idx+1]
        
        ans = []
        for idx in range(len(nums)):
            ans.append(l2r[idx] * r2l[idx])
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#
