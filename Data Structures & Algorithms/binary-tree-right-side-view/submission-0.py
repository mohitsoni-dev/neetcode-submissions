# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.levels = {}
        level = 0
        ans = []
        
        self.dfs(root, 0)

        while True:
            if level not in self.levels:
                break
            ans.append(self.levels[level])
            level += 1
        
        return ans

    def dfs(self, root, level):
        if not root:
            return
        
        if level not in self.levels:
            self.levels[level] = root.val
        
        self.dfs(root.right, level+1)
        self.dfs(root.left, level+1)