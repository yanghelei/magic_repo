#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=30204
#
# [46] 全排列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(result, nums, nums_mask, path):
            if len(path) == len(nums):
                result.append(path[:])
            for i in range(len(nums)):
                if not nums_mask[i]:
                    path.append(nums[i])
                    nums_mask[i] = True
                    backtracking(result, nums, nums_mask, path)
                    path.pop()
                    num_mask[i] = False

        result = []
        num_mask = [False for _ in range(len(nums))]
        backtracking(result, nums, num_mask, [])
        return result


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#