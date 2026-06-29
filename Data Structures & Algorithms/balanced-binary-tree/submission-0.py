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
        if self.globalFlag:
            return 0, False
        
        leftH, flag1 = self.helper(root.left)
        rightH, flag2 = self.helper(root.right)

        # print(leftH, flag1)
        # print(rightH, flag2)
        # print(root.val)

        finalFlag = flag1 and flag2 and (abs(rightH - leftH) <= 1)
        maxHeight = 1 + max(leftH, rightH)
        if not finalFlag:
            self.globalFlag = True
        return maxHeight, finalFlag
