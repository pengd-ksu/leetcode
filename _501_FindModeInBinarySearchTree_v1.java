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
        int prev = l.get(0);
        int count = 1;
        int max = 0;
        for (int i = 1; i < l.size(); i++) {
            if (l.get(i) != prev) {
                if (count > max) {
                    collect = new ArrayList<>();
                    collect.add(prev);
                    max = count;
                } else if (count == max) {
                    collect.add(prev);
                }
                count = 1;
                prev = l.get(i);
            } else {
                count++;
            }
        }
        // Consider the last same elements
        if (count > max) {
            collect = new ArrayList<>();
            collect.add(l.get(l.size()-1));
        } else if (count == max) {
            collect.add(l.get(l.size()-1));
        }
        int[] arr = new int[collect.size()];
        for (int j = 0; j < collect.size(); j++) {
            arr[j] = collect.get(j);
        }
        return arr;
    }
}