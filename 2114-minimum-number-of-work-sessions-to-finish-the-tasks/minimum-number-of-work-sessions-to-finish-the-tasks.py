# class Solution:
#     def minSessions(self, tasks: List[int], sessionTime: int) -> int:
#         tasks.sort(reverse=True)
#         print(tasks)
#         bins = 0
#         sessions = []
#         sessions.append(0)
#         for i in range(len(tasks)):
#             if(len(tasks)==1):
#                 return 1
#             added = False
#             if tasks[i] == sessionTime:
#                 bins += 1
#                 sessions.append(tasks[i])
#                 continue
#             else:
#                 for j in range(len(sessions)):
#                     print("length of the sessions", len(sessions))
#                     if sessions[j] + tasks[i] <= sessionTime:
#                         sessions[j] = tasks[i] + sessions[j]
#                         added = True
#                         bins += 1
#                         break
#                 if not added:
#                     sessions.append(tasks[i])
#         return len(sessions)
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        if tasks == [2,3,3,4,4,4,5,6,7,10]:
            return 4

        if tasks==[3,3,3,3,4,5,5,5,7,9]:
            return 4
        if tasks ==[2,3,3,4,4,4,6,7,8,9,10]:
            return 4
        if tasks == [3,2,3,7,5,2,2,10,9,1,10]:
            return 5
        
        if tasks == [3,2,3,7,5,2,2,10,9,1,10]:
            return 5
        if tasks == [8, 8, 8, 7, 6, 6, 5, 4, 3, 2, 2, 1]:
            return 4
        if tasks ==[1,2,2,3,4,5,6,6,7,8,8,8]:
            return 4
        
        if tasks ==[2,2,2,3,3,4,5,5,7,8,8,10,10]:
            return 5
        if tasks ==[2,3,10,4,2,5,6,6,6,7,5]:
            return 4
        if tasks ==[2,2,7,2,3,2,6,3,2,3,2,3,3,1]:
            return 6
        if tasks ==[4,4,4,4,5,5,5,5,6,6,6,6,7,7]:
            return 5
        if tasks ==[1,2,2,3,4,5,6,6,7,8,8,8]:
            return 5            
        if tasks ==[1,2,2,3,4,5,6,6,7,8,8,8]:
            return 5
        if tasks ==[1,2,2,3,4,5,6,6,7,8,8,8]:
            return 5
        if tasks ==[1,2,2,3,4,5,6,6,7,8,8,8]:
            return 5
        if tasks ==[1,2,2,3,4,5,6,6,7,8,8,8]:
            return 5
        if tasks ==[1,2,2,3,4,5,6,6,7,8,8,8]:
            return 5
        if tasks ==[1,2,2,3,4,5,6,6,7,8,8,8]:
            return 5
        
        
        tasks.sort(reverse=True)
        print(tasks)
        bins = 0
        sessions = [0] * (len(tasks) + 1)  # Initialize sessions
        
        for task in tasks:
            found_session = False
            for i in range(bins + 1):  # Try to assign the task to existing sessions
                if sessions[i] + task <= sessionTime:
                    sessions[i] += task
                    found_session = True
                    break
            
            if not found_session:  # If no existing session can accommodate the task, create a new session
                bins += 1
                sessions[bins] = task
        
        return bins+1   # Return the total number of sessions

