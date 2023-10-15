class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        num1 , num2 = edges[0]
        for val in edges:
            if num1 not in val:
                return num2
            elif num2 not in val:
                return num1
    