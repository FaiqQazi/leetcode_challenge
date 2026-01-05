class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        zeros=[[0]*n for _ in range(m)]
        ones=[[0]*n for _ in range(m)]
        for i in range (len(board)):
            print(f"i is {i}")
            for j in range (len(board[0])):
                print(f"j is {j}")
                if 0<=j+1<n:
                    if board[i][j+1]==0:
                        zeros[i][j]=zeros[i][j]+1
                    if board[i][j+1]==1:
                        ones[i][j]=ones[i][j]+1
                if 0<=j-1<n:
                    if board[i][j-1]==0:
                        zeros[i][j]=zeros[i][j]+1
                    else:
                        print(f"set to 1 {i} and {j-1}")
                        ones[i][j]=ones[i][j]+1
                if 0<=i+1<m:
                    if board[i+1][j]==0:
                        zeros[i][j]=zeros[i][j]+1
                    else:
                        print(f"set to 1 {i+1} and {j}")
                        ones[i][j]=ones[i][j]+1
                if 0<=i-1<m:
                    if board[i-1][j]==0:
                        zeros[i][j]=zeros[i][j]+1
                    else:
                        ones[i][j]=ones[i][j]+1

                if 0 <= i+1 < m and 0 <= j+1 < n:
                    if board[i+1][j+1] == 0:
                        zeros[i][j] += 1
                    else:
                        ones[i][j] += 1

                if 0 <= i+1 < m and 0 <= j-1 < n:
                    if board[i+1][j-1] == 0:
                        zeros[i][j] += 1
                    else:
                        ones[i][j] += 1

                if 0 <= i-1 < m and 0 <= j+1 < n:
                    if board[i-1][j+1] == 0:
                        zeros[i][j] += 1
                    else:
                        ones[i][j] += 1

                if 0 <= i-1 < m and 0 <= j-1 < n:
                    if board[i-1][j-1] == 0:
                        zeros[i][j] += 1
                    else:
                        ones[i][j] += 1

        for i in range (len(board)):
            for j in range (len(board[0])):
                
                print(f"the number of ones in the neighbouring of {i}{j} is {ones[i][j]}")

                if board[i][j]==1 and ones[i][j]<2:
                    board[i][j]=0
                elif board[i][j]==1 and (ones[i][j]==2 or ones[i][j]==3):
                    board[i][j]=1
                elif board[i][j]==1 and ones[i][j]>3:
                    board[i][j]=0
                elif board[i][j]==0 and ones[i][j]==3:
                    board[i][j]=1
                     
                                    

