# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        ans = [[root.val]]

        while queue:
            l = len(queue)
            next_row = []
            for i in range(l):
                node = queue.pop(0)
                if node.left:
                    next_row.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    next_row.append(node.right.val)
                    queue.append(node.right)
            if next_row:
                ans.append(next_row)
        return ans