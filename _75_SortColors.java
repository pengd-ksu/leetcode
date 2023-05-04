class Solution {
    public void sortColors(int[] nums) {
        int r = 0, b = 0, w = 0, n = nums.length;

        // red, white, blue
        // Cut into four sections:
        // 0, r-1; r, n-b-w-1; n-b-w, n-b-1; n-b, n-1
        // Aim: to make the second section not exist
        while (r + w + b < n) {
            int k = n - b - w - 1;
            if (nums[k] == 2) {
                // Color blue
                nums[k] = nums[n-b-1];
                nums[n-b-1] = 2;
                b++;
            } else if (nums[k] == 1) {
                // Color white
                w++;
            } else {
                nums[k] = nums[r];
                nums[r] = 0;
                r++;
            }
        }
    }
}