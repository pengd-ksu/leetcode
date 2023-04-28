class Solution {
    private int count = 0;
    private int[][] board;

    private void placeQueen(int r, int c) {
        board[r][c] = 1;
    }

    private void removeQueen(int r, int c) {
        board[r][c] = 0;
    }

    private boolean isNotUnderAttack(int row, int col, int total) {
        for (int r = 0; r < row; r++) {
            for (int c = 0; c < total; c++) {
                if (board[r][c] == 1) {
                    if ((r==row) ||(c==col)||(Math.abs(row-r)==Math.abs(col-c))) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    private void backtrackQueens(int row, int total) {
        if (row == total) {
            count++;
            return;
        };
        for (int c = 0; c < total; c++) {
            if (isNotUnderAttack(row, c, total)) {
                placeQueen(row, c);
                backtrackQueens(row + 1, total);
                removeQueen(row, c);
            }
        }
        return;
    }

    public int totalNQueens(int n) {
        board = new int[n][n];
        backtrackQueens(0, n);
        return count;
    }
}