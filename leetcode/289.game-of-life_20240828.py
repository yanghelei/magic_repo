#
# @lc app=leetcode.cn id=289 lang=python3
# @lcpr version=30204
#
# [289] 生命游戏
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = {
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        }
        for i in range(m):
            for j in range(n):
                count = 0
                for direction in directions:
                    new_row = i + direction[0]
                    new_col = j + direction[1]
                    if 0 <= new_row < m and 0 <= new_col < n:
                        if abs(board[new_row][new_col]) == 1:
                            count += 1
                if board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = -1  # 活细胞死亡
                if board[i][j] == 0 and count == 3:
                    board[i][j] = -2  # 死细胞复活
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == -2:
                    board[i][j] = 1


# @lc code=end


#
# @lcpr case=start
# [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,0]]\n
# @lcpr case=end

#