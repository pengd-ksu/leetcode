class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int r = m - 1, c = 0;
        // A trick to pick starting point in the bottom left.
        // Since it's largest in the leftest column, if target
        // is smaller, we make it go upper; if target is bigger,
        // we make it only go right.
        while (r >= 0 && c <= n - 1) {
            if (matrix[r][c] == target) {
                return true;
            }
            else if (matrix[r][c] > target) {
                r--;
            } else {
                c++;
            }
        }
        return false;
    }
}