/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */

// approaching with stack

var inorderTraversal = function(root) {
    let result = [];
    let holding_stack = [];
    
    let current_node = root;
    while (current_node != null || holding_stack.length != 0) {
        while (current_node != null) {
            holding_stack.push(current_node);
            current_node = current_node.left;
        }
        current_node = holding_stack.pop();
        result.push(current_node.val);
        current_node = current_node.right;
    }
    return result;
};