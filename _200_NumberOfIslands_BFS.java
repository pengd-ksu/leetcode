class Solution {
    private int[][] DIRECTIONS = {{1,0},{-1,0},{0,1},{0,-1}};
    public int numIslands(char[][] grid) {
        int num = 0;
        int m = grid.length;
        int n = grid[0].length;
        for(int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == '1') {
                    grid[r][c] = '0';
                    num += 1;
                    Queue<int[]> neighbors = new LinkedList<>();
                    neighbors.add(new int[] {r, c});
                    while (!neighbors.isEmpty()) {
                        int[] cell = neighbors.poll();
                        int row = cell[0];
                        int col = cell[1];
                        for (int[] direction: DIRECTIONS) {
                            int nextRow = row + direction[0];
                            int nextCol = col + direction[1];
                            if (nextRow < 0 || nextRow >= m || nextCol < 0 || nextCol >= n || grid[nextRow][nextCol] == '0') {
                                continue;
                            }
                            neighbors.add(new int[] {nextRow, nextCol});
                            // Immediately set to zero, in case back moves leading to duplicate
                            grid[nextRow][nextCol] = '0';
                        }
                    }
                }
            }
        }
        return num;
    }
}