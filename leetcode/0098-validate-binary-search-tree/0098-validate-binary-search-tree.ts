/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isValidBST(root: TreeNode | null): boolean {
        let prev: number | null = null;
    function inOrder(node: TreeNode | null): boolean {
        if (!node) return true;

        if (!inOrder(node.left)) return false;

        if (prev !== null && node.val <= prev) return false;

        prev = node.val;

        return inOrder(node.right);
    }

    // return dfs(root, null, null);
    return inOrder(root);
};