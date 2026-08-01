# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0

        def pathLen(node, val):
            if not node or node.val != val:
                return 0
            return 1 + max(pathLen(node.left,val), pathLen(node.right,val))


        def dfs(node):
            if not node:
                return

            left = pathLen(node.left, node.val)
            right = pathLen(node.right, node.val)
            self.maxi = max(self.maxi,left + right)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.maxi
        