# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.globalFlag = False        
        _, flag = self.helper(root)
        return flag
    def helper(self, root):
        if not root:
            return 0, True
        
        leftH, flag1 = self.helper(root.left)
        if not flag1:
            return 0, False
        rightH, flag2 = self.helper(root.right)
        if not flag2:
            return 0, False

        finalFlag = flag1 and flag2 and (abs(rightH - leftH) <= 1)
        maxHeight = 1 + max(leftH, rightH)
        return maxHeight, finalFlag
