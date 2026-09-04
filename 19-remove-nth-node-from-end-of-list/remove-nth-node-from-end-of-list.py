# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d=ListNode()
        d.next=head
        a=b=d
        for i in range(n+1):
            a=a.next
        while a:
            a=a.next
            b=b.next
        b.next=b.next.next
        return d.next