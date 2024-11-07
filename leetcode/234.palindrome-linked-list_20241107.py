#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30204
#
# [234] 回文链表
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy_head = ListNode()
        dummy_head.next = head

        slow_node, fast_node = dummy_head, dummy_head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        temp_dummy_head = slow_node
        cur_node = temp_dummy_head.next
        while cur_node and cur_node.next:
            temp = cur_node.next.next
            cur_node.next.next = temp_dummy_head.next
            temp_dummy_head.next = cur_node.next
            cur_node.next = temp

        node1, node2 = dummy_head.next, temp_dummy_head.next
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1, node2 = node1.next, node2.next

        return True


# @lc code=end


#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#
