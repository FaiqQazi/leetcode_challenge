class Solution:
    def convert(self, s: str, numRows: int) -> str:
        numCols=0
        # if len(s)==1 or len(s)==2 or len(s)==3:
        #     return s
        # for i in range(1,len(s)+1):
        #     if i%(numRows+(numRows-2))==0:
        #         numCols=numCols+(1+(numRows-2))
        #         # print(f"i is {i} and numcols {numCols}")
        # if (i%(numRows+(numRows-2)))<=numRows:
        #     numCols=numCols+1
        # else:
        #     numCols=numCols+((i%(numRows+(numRows-2)))-numRows)
        
        # # print(i%(numRows+(numRows-2)))
        # # print(f"the num of columns are {numCols}")
        numCols = len(s)   # worst case
        arr = [[""] * numCols for _ in range(numRows)]
        # print(arr)
        # now we have the arry in place now we just need to fill it in the given order
        r=0
        c=0
        final_string=""
        i=0
        while i!=len(s):
            # print(s[i])
            for m in range(0,numRows):
                if i==len(s):
                    break
                arr[m][c]=s[i]
                i=i+1
                # print(f"arr[m][c] {arr[m][c]} has been appended to arr at positon {m}{c}")
                # print(f"i is {i}")
            c=c+1   
            for j in range(0,(numRows-2)):
                if i==len(s):
                    break
                arr[(m-j)-1][c]=s[i]
                # print(f"arr[(m+j)-1][(m+j)-1] is {arr[(m+j)-1][c]} has been appended to arr at position {(m+j)-1} and {c}")
                # print(f"i is {i}")
                i=i+1
                c=c+1

            
        # print(f"at the end of that the arr is {arr}")
        for i in range(len(arr)):
            for j in range(numCols):
                final_string += str(arr[i][j])
        return final_string


                

        