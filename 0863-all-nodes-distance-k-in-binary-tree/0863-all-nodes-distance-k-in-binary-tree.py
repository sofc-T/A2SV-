# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        parent = {}
        q = deque()
        q.append(root)
        while(q):
            node = q.popleft()
            if(node.left):
                parent[node.left] = node
                q.append(node.left)

            if(node.right):
                parent[node.right] = node
                q.append(node.right)
        # print(q).
        visited = set()
        q.append(target)
        visited.add(target)
        distance = 0
        while(q and distance != k):
            distance+=1
            temp_q = deque()
            while(q):
                node = q.popleft()
                if(node in parent and parent[node] not in visited):
                    temp_q.append(parent[node])
                    visited.add(parent[node])
                if(node.left and node.left not in visited):
                    temp_q.append(node.left)
                    visited.add(node.left)
                if(node.right and node.right not in visited):
                    temp_q.append(node.right)
                    visited.add(node.right)
            q = temp_q
        res = []
        for node in q:
            res.append(node.val)
        return res


