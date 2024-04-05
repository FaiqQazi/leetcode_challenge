
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if head is None:
#             return False

#         pointer1 = head
#         pointer2 = head.next
#         j = 0
       
#         while pointer1.next is not None and pointer2.next.next is not None:
#             if pointer1 == pointer2:
#                 return True
#             pointer1 = pointer1.next
#             pointer2 = pointer2.next.next
            
    
#         return False
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        slow_pointer = head
        fast_pointer = head.next
        
        while fast_pointer and fast_pointer.next:
            if slow_pointer == fast_pointer:
                return True
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        return False
