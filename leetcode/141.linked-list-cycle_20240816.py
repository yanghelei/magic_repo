#
# @lc app=leetcode.cn id=141 lang=python3
# @lcpr version=30204
#
# [141] 环形链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return head

        slow_node = head
        fast_node = head.next

        while fast_node and fast_node.next:
            if fast_node == slow_node:
                return True
            else:
                slow_node = slow_node.next
                if fast_node.next:
                    fast_node = fast_node.next.next
                else:
                    return False

        return False


# @lc code=end


#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#