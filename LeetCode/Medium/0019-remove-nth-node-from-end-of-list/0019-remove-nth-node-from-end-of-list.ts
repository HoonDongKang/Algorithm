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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    let first = head;

    for (let i = 0; i < n; i++) {
        first = first?.next!;
    }

    let dummy = new ListNode(0, head);
    let second = dummy;

    while (first) {
        first = first.next;
        second = second.next!;
    }

    second.next = second.next?.next || null;
    return dummy.next;
};