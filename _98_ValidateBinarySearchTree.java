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
        if (root == null) return true;
        if (!compareNode(root.val, true, root.left)
            || !compareNode(root.val, false, root.right)) {
                return false;
        }
        return isValidBST(root.left) 
                && isValidBST(root.right);
    }

    public boolean compareNode(int val, boolean left, TreeNode node) {
        if (node == null) return true;
        if ((left && node.val >= val)
            || (!left && node.val <= val)) {
            return false;
        } else {
            return compareNode(val, left, node.left)
                    && compareNode(val, left, node.right);
        }
    }
}