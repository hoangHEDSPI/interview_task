/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

function printListNode(list_node) {
    if (list_node == null) return;
    while (list_node.next != null) {
        console.log(list_node.val);
        list_node = list_node.next;
    }
}

/* recursion and iterative solution can be used on this problem */


/* iterative solution */

var mergeTwoLists = function(l1, l2) {
    if (l1 == null) return l2;
    if (l2 == null) return l1;

    res_node = new ListNode(0);
    curr_node = res_node;
    while (l1.next != null && l2.next != null) {
        if (l1.val <= l2.val) {
            curr_node.next = l1;
            l1 = l1.next;
        }
        else {
            curr_node.next = l2;
            l2 = l2.next;
        }
        curr_node = curr_node.next;
    }

    curr_node.next = (l1 == null) ? l2 : l1;

    printListNode(res_node.next);
    return res_node.next;

};
