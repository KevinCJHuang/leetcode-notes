# Reorder List (https://leetcode.com/problems/reorder-list/)
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return head

        size = 1
        curHead = head
        while curHead.next is not None:
            size += 1
            curHead = curHead.next
        if size <= 2:
            return
        curHead.next = ListNode(0, None)
        head = ListNode(0, head)
        size += 2

        midHead = head
        prevHead = None
        for i in range(ceil(size/2)):
            prevHead = midHead
            midHead = midHead.next

        prevHead.next = None

        # midHead is now in the middle
        prevHead = midHead
        curHead = midHead.next # 5 -> 6
        while curHead and curHead.next:
            nextHead = curHead.next
            curHead.next = prevHead
            prevHead = curHead
            curHead = nextHead
        curHead.next = prevHead

        leftHead = head
        rightHead = curHead
        for i in range (size//2):
            leftNextHead = leftHead.next
            rightNextHead = rightHead.next
            leftHead.next = rightHead
            rightHead.next = leftNextHead
            leftHead = leftNextHead
            rightHead = rightNextHead
