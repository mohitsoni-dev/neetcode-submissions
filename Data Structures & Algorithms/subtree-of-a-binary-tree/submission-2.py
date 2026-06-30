# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.code = ""
        self.res = False
        self.code = self.serialize(subRoot)
        self.serialize(root)

        return self.res
        
    def serialize(self, root, code=""):
        if not root:
            ans = "#"
        else:
            ans = str(root.val) + ", " + self.serialize(root.left) + ", " + self.serialize(root.right)
        
        if self.code == ans:
            self.res = True
        return ans
