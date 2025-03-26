/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let dummy = new ListNode();
    let curNode = dummy;
    let carry = 0;

    while (l1 || l2 || carry) {
        let sum = (l1?.val ?? 0) + (l2?.val ?? 0) + carry;
        let nextVal = sum % 10;
        carry = Math.floor(sum/10);

        curNode.next = new ListNode(nextVal);
        curNode = curNode.next;

        if (l1) l1 = l1.next;
        if (l2) l2 = l2.next;
    }
    return dummy.next;
};