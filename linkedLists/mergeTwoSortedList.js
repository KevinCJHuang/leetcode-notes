// Merge TwoSorted List (https://leetcode.com/problems/merge-two-sorted-lists/)
/*
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
*/


/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
 var mergeTwoLists = function(list1, list2) {
    var head = new ListNode();
    var curHead = head;
    while (list1 && list2) {
        if (list1.val > list2.val) {
            curHead.next = new ListNode(list2.val);
            list2 = list2.next;
        } else {
            curHead.next = new ListNode(list1.val);
            list1 = list1.next;
        }
        curHead = curHead.next;
    }
    if (list1) {
        curHead.next = list1;
    }
    if (list2) {
        curHead.next = list2;
    }
    return head.next;
};
