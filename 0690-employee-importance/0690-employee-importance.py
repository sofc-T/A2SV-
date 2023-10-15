"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {employee.id: employee for employee in employees}
        importance = 0
        stack = [id]
        while stack:
            curr_id = stack.pop()
            employee = d[curr_id]
            importance += employee.importance
            stack.extend(employee.subordinates)
        return importance
        