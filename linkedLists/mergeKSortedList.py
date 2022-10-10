# Merge k Sorted Lists https://leetcode.com/problems/merge-k-sorted-lists/
#
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return
        minHeap = PriorityQueue()
        for i in range(len(lists)):
            if lists[i] is not None:
                minHeap.put((lists[i].val, i))
                lists[i] = lists[i].next

        head = ListNode()
        curHead = head
        while (minHeap.qsize()):
            val, index = minHeap.get()
            curHead.next = ListNode(val, None)
            curHead = curHead.next
            if (lists[index]):
                minHeap.put((lists[index].val, index))
                lists[index] = lists[index].next
        return head.next
