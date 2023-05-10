class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        // Key observation: min diff happen between adjacent elements
        // in a sorted array
        Arrays.sort(arr);
        List<List<Integer>> res = new ArrayList();
        int minPair = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length - 1; i++) {
            minPair = Math.min(minPair, arr[i+1] - arr[i]);
        }
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i+1] - arr[i] == minPair) {
                res.add(Arrays.asList(arr[i], arr[i+1]));
            }
        }
        return res;
    }
}