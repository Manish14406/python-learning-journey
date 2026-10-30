# Definition for singly-linked list.
head = [1,2,3,4,5]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head:None) ->None:
        current = head
        while current and current.next:
            current.next = current
        return head

