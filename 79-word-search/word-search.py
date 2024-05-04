# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         #find the element in the board
#         r=0
#         c=0
#         thebool=False
#         checked=[]
#         strnum=0
#         length=len(board)
#         print ("lenght of the board is ",length)
#         if  len(word)==1:
#             if word[0]==board[0][0]:
#                 return True
#             else:
#                 return False

#         for n in range(1+(length * length)):

#             found = False
#             visited=[]
#             for ridx, row in enumerate(board):
#                 for cidx, column in enumerate(row):
#                     if [ridx, cidx] in checked:
#                         print("continuing")
#                         continue
#                     if column == word[strnum]:
#                         found = True
#                         checked.append([ridx, cidx])
#                         print("checked is")
#                         print(checked)
#                         print("Starting at index ", ridx, cidx, "boardij=word", column, word[strnum])
#                         r = ridx
#                         c = cidx
#                         strnum += 1
#                         print("strnum is ", strnum)
#                         break
#                 if found:
#                     print("breaking")
#                     break

#             print("len of word")
#             print (len (word))
#             for m in range(len(word)):
#                 print("statring the second loop")
#                 if( r+1<length and board[r+1][c] and [r+1,c]not in visited):
#                     if(board[r+1][c]==word[strnum]):
#                         visited.append([r+1,c])
#                         print("found the ",board[r+1][c],"in the right")
#                         strnum+=1
#                         r=r+1
#                         c=c
#                         thebool=True
#                 if(r-1>0 and board[r-1][c] and [r-1,c]not in visited):
#                     if(board[r-1][c]==word[strnum]):
#                         visited.append([r-1,c])
#                         print("found the ",board[r-1][c],"in the left")
#                         strnum+=1
#                         r=r-1
#                         c=c
#                         thebool=True
#                 if(c+1<length and board[r][c+1] and [r,c+1]not in visited):
#                     if(board[r][c+1]==word[strnum]):
#                         visited.append([r,c+1])
#                         print("found the ",board[r][c+1],"in the down")
#                         strnum+=1
#                         r=r
#                         c=c+1
#                         thebool=True
#                 if(c-1>0 and board[r][c-1]and [r,c-1]not in visited):
#                     if(board[r][c-1]==word[strnum]):
#                         visited.append([r,c-1])
#                         print("found the ",board[r][c-1],"in the topt")
#                         strnum+=1
#                         r=r
#                         c=c-1
#                         thebool=True
#                 if thebool==False:
#                     strnum=0
#                     break
#                 if thebool==True:
#                     print("str num and len word ",strnum,len(word))
#                     if strnum==len(word):
#                         return True
#                     thebool=False
#         return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length = len(board)
        if len(word) == 1:  # Base case: Single character word
            for row in board:
                if word in row:
                    return True
            return False

        for ridx, row in enumerate(board):
            for cidx, column in enumerate(row):
                if column == word[0]:  # Start of word found
                    if self.dfs(board, word, ridx, cidx, set()):
                        return True
        return False

    def dfs(self, board, word, r, c, visited):
        if not (0 <= r < len(board) and 0 <= c < len(board[0])) or (r, c) in visited:
            return False  # Out of bounds or already visited
        
        if board[r][c] == word[0]:
            if len(word) == 1:  # Base case: Single character word
                return True
            
            visited.add((r, c))  # Mark current position as visited
            
            # Recursively search in all four directions
            if (self.dfs(board, word[1:], r + 1, c, visited) or
                self.dfs(board, word[1:], r - 1, c, visited) or
                self.dfs(board, word[1:], r, c + 1, visited) or
                self.dfs(board, word[1:], r, c - 1, visited)):
                return True  # If word is found, return True
            
            visited.remove((r, c))  # Backtrack: Remove current position from visited set
        
        return False
