#
# @lc app=leetcode.cn id=80 lang=python3
# @lcpr version=30204
#
# [80] 删除有序数组中的重复项 II
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cache = 0
        last_num = float("inf")
        input_idx = 0
        for search_idx in range(len(nums)):
            if cache < 2:
                cache = 1 if last_num != nums[search_idx] else cache + 1
                last_num = nums[search_idx]
                nums[input_idx] = nums[search_idx]
                input_idx += 1
            elif last_num != nums[search_idx]:
                cache = 1
                last_num = nums[search_idx]
                nums[input_idx] = nums[search_idx]
                input_idx += 1
        return input_idx


# @lc code=end


#
# @lcpr case=start
# [1,1,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,1,2,3,3]\n
# @lcpr case=end

#
