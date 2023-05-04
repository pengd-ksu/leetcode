class Solution {
    public void sortColors(int[] nums) {
        // The 3 partition way proposed by Dijkstra
        /*
        Entries from 0 up to (but not including) i are values less than mid,
        entries from i up to (but not including) j are values equal to mid,
        entries from j up to (and including) k are values not yet sorted, and
        entries from k + 1 to the end of the array are values greater than mid.
        */
        int i = 0, j = 0, k = nums.length - 1;
        int mid = 1;
        // Invariant: i <= j <= k
        while (j <= k) {
            if (nums[j] < mid) {
                this.swap(nums, i, j);
                i++;
                j++;
            } else if (nums[j] > mid) {
                this.swap(nums, j, k);
                k--;
            } else {
                j++;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}