# 19. Remove Nth Node From End of List (https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        dummyHead = ListNode(0, head)
        curHead = dummyHead
        rv = dummyHead
        diff = 0
        while curHead.next is not None:
            curHead = curHead.next
            if diff == n:
                rv = rv.next
            else:
                diff += 1

        rv.next = rv.next.next
        return dummyHead.next
