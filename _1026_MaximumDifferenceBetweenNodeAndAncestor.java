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
    private int recursive(TreeNode node, int curMin, int curMax) {
        if (node == null) return curMax - curMin;
        curMin = Math.min(node.val, curMin);
        curMax = Math.max(node.val, curMax);
        return Math.max(recursive(node.left, curMin, curMax), 
                        recursive(node.right, curMin, curMax));
    }

    public int maxAncestorDiff(TreeNode root) {
        if (root == null) return 0;
        return recursive(root, root.val, root.val);
    }
}