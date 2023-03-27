class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int[][] dist = new int[m][n];
        int[][] direction = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        Queue<int[]> q = new LinkedList<>();
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                dist[r][c] = Integer.MAX_VALUE;
            }
        }
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (mat[row][col] == 0) {
                    dist[row][col] = 0;
                    q.add(new int[] {row, col});
                }
            }
        }
        while (!q.isEmpty()) {
            int[] cell = q.remove();
            for (int[] dir : direction) {
                int nextR = cell[0] + dir[0];
                int nextC = cell[1] + dir[1];
                if (nextR >= 0 && nextC >= 0 && nextR < m && nextC < n) {
                    if (dist[nextR][nextC] > dist[cell[0]][cell[1]] + 1) {
                        dist[nextR][nextC] = dist[cell[0]][cell[1]] + 1;
                        q.add(new int[] {nextR, nextC});
                    }
                }
            }
        }
        return dist;
    }
}