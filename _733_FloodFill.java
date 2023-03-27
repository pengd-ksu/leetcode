class Solution {
    public void dfs(int[][] image, int r, int c, int color, int newColor) {
        // In case went into endless loop among same color neighbors.
        if (image[r][c] != color) {
            return;
        }
        image[r][c] = newColor;
        if (r >= 1) {
            dfs(image, r-1, c, color, newColor);
        }
        if (c >= 1) {
            dfs(image, r, c-1, color, newColor);
        }
        if (r+1 < image.length) {
            dfs(image, r+1, c, color, newColor);
        }
        if (c+1 < image[0].length) {
            dfs(image, r, c+1, color, newColor);
        }
    }

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        // If already flood fill (color == image[sr][sc]), just return image
        if (color != image[sr][sc]) {
            dfs(image, sr, sc, image[sr][sc], color);;
        }
        return image;
    }
}