class Solution {
    public int[] merge_sort(int[] input) {
        if (input.length <= 1) {
            return input;
        }
        int mid = input.length / 2;
        int []left = merge_sort(Arrays.copyOfRange(input, 0, mid));
        int []right = merge_sort(Arrays.copyOfRange(input, mid, input.length));

        return merge(left, right);
    }
    public int[] merge(int[] left, int[] right) {
        int [] res = new int[left.length + right.length];
        int lid = 0, rid = 0, resid = 0;
        while (lid < left.length && rid < right.length) {
            if (left[lid] < right[rid]) {
                res[resid++] = left[lid++];
            } else {
                res[resid++] = right[rid++];
            }
        }
        while (lid < left.length) {
            res[resid++] = left[lid++];
        }
        while (rid < right.length) {
            res[resid++] = right[rid++];
        }
        return res;
    }
public int[] sortArray(int[] nums) {
    return merge_sort(nums);
}
}