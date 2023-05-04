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
    List<Integer> collect = new ArrayList<>();
    TreeNode prev;
    int count = 0;
    int maxCount = 0;

    private void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        if (prev == null || node.val != prev.val) {
            count = 1;
            prev = node;
        } else {
            count++;
        }
        if (count > maxCount) {
            collect.clear();
            collect.add(node.val);
            maxCount = count;
        } else if (count == maxCount) {
            collect.add(node.val);
        }
        inorder(node.right);
    } 

    public int[] findMode(TreeNode root) {
        inorder(root);

        int[] arr = new int[collect.size()];
        for (int j = 0; j < collect.size(); j++) {
            arr[j] = collect.get(j);
        }
        return arr;
    }
}