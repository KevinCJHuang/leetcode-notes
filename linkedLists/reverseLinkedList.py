# 217. Contains Duplicate https://leetcode.com/problems/reverse-linked-list/
# Given the head of a singly linked list, reverse the list, and return the reversed list.

#include <unordered_set>
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curHead = head
        prevHead = None
        while (curHead.next):
            nextHead = curHead.next
            curHead.next = prevHead
            prevHead = curHead
            curHead = nextHead
        curHead.next = prevHead
        return curHead
