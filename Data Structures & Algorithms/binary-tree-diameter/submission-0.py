# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    cache = {}
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.cache = {}
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left + right, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    
    def maxDepth(self, root):
        if not root:
            return 0
        if root in self.cache:
            return self.cache[root]
        ans = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        self.cache[root] = ans
        return ans