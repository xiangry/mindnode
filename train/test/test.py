#! --*-- coding: utf-8 --*--
__author__ = 'gaoxingsheng'


def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """

    for line in board:
        count = {}
        for n in line:
            count[n] = count.get(n, 0) + 1
        for n in count:
            if n != '.' and count[n] >= 2:
                return False, 1, line

    for i in xrange(len(board[0])):
        count = {}
        for line in board:
            count[line[i]] = count.get(line[i], 0) + 1

        print i, count

        for n in count:
            if n != '.' and count[n] >= 2:
                return False, 2, i

    for x in xrange(len(board) / 3):
        for y in xrange(len(board[0]) / 3):
            count = {}
            for i in xrange(3):
                for j in xrange(3):
                    n = board[x * 3 + i][y * 3 + j]
                    count[n] = count.get(n, 0) + 1

            for n in count:
                if n != '.' and count[n] >= 2:
                    return False, 3, x, y

    return True


board = [["8","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))