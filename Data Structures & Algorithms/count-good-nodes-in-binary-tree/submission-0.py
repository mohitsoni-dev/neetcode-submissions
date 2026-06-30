# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float("-inf"))
    
    def dfs(self, root, max_till):
        if not root:
            return 0
        
        val = root.val
        ans = 0

        if val >= max_till:
            ans = 1

        return ans + self.dfs(root.left, max(max_till, val)) + self.dfs(root.right, max(max_till, val))
        
