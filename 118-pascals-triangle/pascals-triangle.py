#make a list of list and then implement 
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dlist=[]
        i=0
        while (i<numRows):
            dlist.append([])
            i+=1
        i=0
        # while(i<numRows):
        #     dlist[i].append(None)
        #     i+=1
        #start with 1
        i=1
        dlist[0].append(1)
        print(dlist)
        while(i<numRows):
            x=len(dlist[i-1])
            print(x)
            j=0
            while(j<=x):
                if(j!=0 and j!=x):
                    print("printing the down")
                    print(dlist[i-1][j]+dlist[i-1][j-1])
                    dlist[i].append(dlist[i-1][j]+dlist[i-1][j-1])
                    j+=1
                elif(j==0):
                    dlist[i].append(dlist[i-1][0])
                    j+=1
                elif(j==x):
                    dlist[i].append(dlist[i-1][x-1])
                    j+=1
            i+=1
            print(dlist)
        return dlist

