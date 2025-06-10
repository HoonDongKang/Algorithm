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

/**
 Do not return anything, modify head in-place instead.
 */
function reorderList(head: ListNode | null): void {
    if (!head || !head.next) return;

    const stack: ListNode[] = [];
    let node: ListNode | null = head;

    while (node) {
        stack.push(node);
        node = node.next;
    }

    const length = stack.length;
    node = head;

    for (let i = 0; i < Math.floor(length / 2); i++) {
        const tail = stack.pop()!;
        const next: ListNode | null = node.next;

        node.next = tail;
        tail.next = next;

        node = next!;
    }

    node.next = null;
};