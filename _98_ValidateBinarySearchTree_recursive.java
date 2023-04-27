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
    public boolean isValidBST(TreeNode root) {
        // For the root, there's no upper nor lower limit to compare with
        return validate(root, null, null);
    }

    public boolean validate(TreeNode node, Integer low, Integer high) {
        // Empty tree is a sub BST
        if (node == null) return true;
        // Compare with upper and lower limit
        if ((low != null && node.val <= low)
            || (high != null && node.val >= high)) {
                return false;
        }
        // Go left with a lower limit; go right with a higher limit
        return validate(node.right, node.val, high) && validate(node.left, low, node.val);
    }
}