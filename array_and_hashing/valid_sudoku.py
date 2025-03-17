from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_sets_row = set()
        hash_sets_col = set()
        hash_sets_square = set()

        for row in range(len(board)):
            for col in range(len(board)):
                val = board[row][col]
                square = (row // 3) * 3 + (col // 3)

                if (row, val) in hash_sets_row and val != ".":
                    return False
                else:
                    hash_sets_row.add((row, val))

                if (col, val) in hash_sets_col and val != ".":
                    return False
                else:
                    hash_sets_col.add((col, val))

                if (square, val) in hash_sets_square and val != ".":
                    return False
                else:
                    hash_sets_square.add((square, val))

        return True


def main():
    sol = Solution()

    board1 = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
              ["4", ".", ".", "5", ".", ".", ".", ".", "."],
              [".", "9", "8", ".", ".", ".", ".", ".", "3"],
              ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
              [".", ".", ".", "8", ".", "3", ".", ".", "5"],
              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", ".", ".", ".", ".", ".", "2", ".", "."],
              [".", ".", ".", "4", "1", "9", ".", ".", "8"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    board2 = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
              ["4", ".", ".", "5", ".", ".", ".", ".", "."],
              [".", "9", "1", ".", ".", ".", ".", ".", "3"],
              ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
              [".", ".", ".", "8", ".", "3", ".", ".", "5"],
              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", ".", ".", ".", ".", ".", "2", ".", "."],
              [".", ".", ".", "4", "1", "9", ".", ".", "8"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(sol.isValidSudoku(board2))


if __name__ == '__main__':
    main()
