class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls = [ind for ind in range(len(boxes)) if boxes[ind] == "1"]
        ans = []
        for ind in range(len(boxes)):
            ans.append(sum(abs(ind - val) for val in balls))
        return ans