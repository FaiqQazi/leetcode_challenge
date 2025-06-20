# class Solution:
#     def check_all_zeros(self, img1):
#         for i in range(len(img1)):
#             for j in range(len(img1[0])):
#                 if(img1[i][j] !=0):
#                     return False
#         return True
#     def checkoverlap(self  , img1 , img2, direction):
#         rows=len(img1)
#         is_zero=False
#         columns=len(img1[0])
#         if direction == "left":
#             for i in range(0,rows):
#                 for j in range(1,columns):
#                     img1[i][j-1]=img1[i][j]
#             is_zero=self.check_all_zeros(img1)
#         if direction=="right":
#             for i in range(0,rows):
#                 for j in range(columns - 2, -1, -1):
#                     img1[i][j + 1] = img1[i][j]
#         if direction =="up":
#             for i in range(1,rows):
#                 for j in range(0,columns):
#                     img1[i - 1][j] = img1[i][j]
#         if direction=="down":
#             for i in range(rows - 2, -1, -1):
#                 for j in range(columns):
#                     img1[i + 1][j] = img1[i][j]

#         if is_zero:
#             return
#         else:
#             # calculate the overalp between the arrays
#             total=0
#             for i in range(len(img1)):
#                 for j in range(len(img1[0])):
#                     if img1[i][j]==img2[i][j] and img1[i][j]==1 and img2[i][j]==1:
#                         total=total+1
#             self.arr.append(total)
#             self.checkoverlap(img1,img2,"left")
#             self.checkoverlap(img1,img2,"right")
#             self.checkoverlap(img1,img2,"up")
#             self.checkoverlap(img1,img2,"down")

#     def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
#         # I think it will be a recursive solution 
#         self.arr=[]
#         self.checkoverlap(img1,img2,"left")
#         self.checkoverlap(img1,img2,"right")
#         self.checkoverlap(img1,img2,"up")
#         self.checkoverlap(img1,img2,"down")
#         return max(arr)

# recursion is not the right approach 
class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n=len(img1)
        max_shift=0
        for dx in range(-n,n+1):
            for dy in range(-n,n+1):
                max_shift=max(max_shift,self.overlap(img1,img2,dx,dy))
        return max_shift
    def overlap(self,img1,img2,dx,dy):
        overlap=0
        for i in range(len(img1)):
            for j in range(len(img1)):
                if 0 <= i+dx < len(img1) and 0 <= j+dy < len(img1):
                    if img1[i+dx][j+dy]==1 and img2[i][j]==1:
                        overlap+=1
        return overlap