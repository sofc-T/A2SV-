# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        totalSum = [0]
        self.helper(root, totalSum, 0)
        return totalSum[0]

    def helper(self, root: TreeNode, totalSum: List[int], sumTillCurrNode: int) -> None:
        if root is None:
            return
        sumTillCurrNode = sumTillCurrNode * 10 + root.val
        if root.left is None and root.right is None:
            totalSum[0] += sumTillCurrNode
        self.helper(root.left, totalSum, sumTillCurrNode)
        self.helper(root.right, totalSum, sumTillCurrNode)