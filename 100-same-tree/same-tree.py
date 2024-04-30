# l1 = []
# l2 = []
# l3 = [] 
# l4 = []
# l5 = []
# l6 = []

# class Solution:
#     def inorderp(self, p):
#         if p is None:
#             return
#         self.inorderp(p.left)
#         l1.append(p.val)
#         self.inorderp(p.right)
        
#     def preorderp(self, q):
#         if q is None:
#             return
#         l2.append(q.val)
#         self.preorderp(q.left)
#         self.preorderp(q.right)
        
#     def inorderq(self, p):
#         if p is None:
#             return
#         self.inorderq(p.left)
#         l3.append(p.val)
#         self.inorderq(p.right)
        
#     def postorderp(self, p):
#         if p is None:
#             return
#         self.postorderp(p.left)
#         self.postorderp(p.right)
#         l5.append(p.val)
        
#     def postorderq(self, p):
#         if p is None:
#             return
#         self.postorderq(p.left)
#         self.postorderq(p.right)
#         l6.append(p.val)
        
#     def preorderq(self, q):
#         if q is None:
#             return
#         l4.append(q.val)
#         self.preorderq(q.left)
#         self.preorderq(q.right)
        
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if(p is None and q is None ):
#             return True
#         if p and not p.left and not p.right and q and not q.left and not q.right:
#             return p.val == q.val
#         self.inorderp(p)
#         self.inorderq(q)
#         self.preorderp(p)
#         self.preorderq(q)
#         self.postorderp(p)
#         self.postorderq(q)
        
#         lists = [l1, l3, l2, l4, l5, l6]
#         print('\n'.join([' '.join(map(str, lst)) for lst in lists]))
        
#         return l1 == l3 and l2 == l4 and l5 == l6
class Solution:
    # Your other methods...

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: both trees are empty, so they are identical
        if p is None and q is None:
            return True
        
        # Check if either tree is empty or their values are different
        if p is None or q is None or p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
