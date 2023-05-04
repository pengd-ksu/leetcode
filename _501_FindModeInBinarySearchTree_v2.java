/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> l = new ArrayList<>();

    public void trans(TreeNode node) {
        if (node != null) {
            trans(node.left);
            l.add(node.val);
            trans(node.right);
        }
    }

    public int[] findMode(TreeNode root) {
        trans(root);
        List<Integer> collect = new ArrayList<>();
        int prev = Integer.MIN_VALUE;
        int count = 0;
        int maxCount = 0;
        for (int i = 0; i < l.size(); i++) {
            if (prev == Integer.MIN_VALUE || l.get(i) != prev) {
                count = 1;
                prev = l.get(i);
            } else {
                count++;
            }
            // We update collect every time, so combine the update during
            // the procedure and after the procedure in last version.
            if (count > maxCount) {
                collect.clear();
                collect.add(prev);
                maxCount = count;
            } else if (count == maxCount) {
                collect.add(prev);
            }                   
        }

        int[] arr = new int[collect.size()];
        for (int j = 0; j < collect.size(); j++) {
            arr[j] = collect.get(j);
        }
        return arr;
    }
}