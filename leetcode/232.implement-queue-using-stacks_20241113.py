#
# @lc app=leetcode.cn id=232 lang=python3
# @lcpr version=30204
#
# [232] 用栈实现队列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self.move()
        return self.stack2.pop()

    def peek(self) -> int:
        self.move()
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

    def move(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end


#
# @lcpr case=start
# ["MyQueue", "push", "push", "peek", "pop", "empty"][[], [1], [2], [], [], []]\n
# @lcpr case=end

#