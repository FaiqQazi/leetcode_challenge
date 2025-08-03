class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key=lambda x: (x[0], -x[1]))
        # visited=[]
        # # print("the intervals after the sorting are")
        # # print(intervals)
        # for i in range(len(intervals)-1):
        #     # print("now checking for")
        #     # print(intervals[i])
        #     for j in range(i,len(intervals)):
        #         # print(f"checking {intervals[j]} with in the {intervals[i]}")
        #         if intervals[j][1]<=intervals[i][1] and not intervals[j] in visited and not (intervals[j][0]==intervals[i][0] and intervals[j][1]==intervals[i][1]):
        #             # print(f" {intervals[j]} is inside {intervals[i]}")
        #             visited.append(intervals[j])
        #             # print("after removing the intervals is")
        #             # print(intervals)
        # answer=[]
        # for n in intervals:
        #     if n in visited:
        #         continue
        #     answer.append(n)
        # return len(answer)


        intervals.sort(key=lambda x: (x[0], -x[1]))
        visited=[]
        prev=intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][1]<=prev[1]:
                visited.append(intervals[i]) 
            else:
                prev=intervals[i]         
        
        answer=[]
        for n in intervals:
            if n in visited:
                continue
            answer.append(n)
        return len(answer)

        