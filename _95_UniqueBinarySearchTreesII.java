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
    private LinkedList<TreeNode> generateLinkedTrees(int left, int right) {
        LinkedList<TreeNode> allTrees = new LinkedList<>();
        if (left > right) {
            // In fact this func will return allTrees here, since it won't
            // enter the next for loop because left > right.
            // The null is for corner case when left or right is chosen
            // as root, and they will lack either left or right children
            allTrees.add(null);
        }
        for (int i = left; i <= right; i++) {
            LinkedList<TreeNode> leftTrees = generateLinkedTrees(left, i - 1);
            LinkedList<TreeNode> rightTrees = generateLinkedTrees(i + 1, right);
            for (TreeNode l : leftTrees) {
                for (TreeNode r : rightTrees) {
                    TreeNode root = new TreeNode(i);
                    root.left = l;
                    root.right = r;
                    allTrees.add(root);
                }
            }
        }
        return allTrees;
    }
    public List<TreeNode> generateTrees(int n) {
        return generateLinkedTrees(1, n);
    }
}