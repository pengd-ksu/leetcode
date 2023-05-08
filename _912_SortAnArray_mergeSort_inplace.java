class Solution {
    public void merge_sort(int[] input) {
        if (input.length <= 1) {
            return;
        }
        int mid = input.length / 2;
        int []left = Arrays.copyOfRange(input, 0, mid);
        int []right = Arrays.copyOfRange(input, mid, input.length);
        merge_sort(left);
        merge_sort(right);
        merge(left, right, input);
    }
    public void merge(int[] left, int[] right, int[] input) {
        int lid = 0, rid = 0, resid = 0;
        while (lid < left.length && rid < right.length) {
            if (left[lid] < right[rid]) {
                input[resid++] = left[lid++];
            } else {
                input[resid++] = right[rid++];
            }
        }
        while (lid < left.length) {
            input[resid++] = left[lid++];
        }
        while (rid < right.length) {
            input[resid++] = right[rid++];
        }
    }
    public int[] sortArray(int[] nums) {
        merge_sort(nums);
        return nums;
    }
}