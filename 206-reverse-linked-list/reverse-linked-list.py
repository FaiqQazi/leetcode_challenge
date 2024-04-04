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
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         current = head
#         prev = None
#         if head:
#             next_node = head.next
#         else:
#             return None  # Return None if head is None
#         while current.next:
#             current.next = prev
#             prev = current
#             current = next_node
#             next_node = current.next
#         current.next = prev  # Update the last node's next pointer
#         return current  # Return the new head
