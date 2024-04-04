# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        prev=None
        if(head!=None):
            next=current.next
        else:
            return
        while(current.next!=None):
            current.next=prev
            prev=current
            current=next
            next=next.next
        current.next=prev
        return current
