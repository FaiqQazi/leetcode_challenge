"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque
class Solution:
    def getemployee(self, employees: List['Employee'], id: int) -> int:
        for emp in employees:
            if emp.id==id:
                return emp
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        earr=deque()
        theemp=self.getemployee(employees,id)
        earr.append(theemp)
        total_value=0
        while earr:           
            e=earr.popleft()
            print("the importance of e is ")
            print(e.importance)
            print("the id of e is ")
            print(e.id)
            total_value=total_value+e.importance
            print("the total value is now")
            print(total_value)
            print("the current employee id is ")
            print(e.id)
            for s in e.subordinates:
                print("s is ")
                print(s)
                sub=self.getemployee(employees,s)
                print("the employee id of the subordinate is ")
                print(sub.id)
                earr.append(sub)
            print("the array is")
            print(earr)
        return total_value







        