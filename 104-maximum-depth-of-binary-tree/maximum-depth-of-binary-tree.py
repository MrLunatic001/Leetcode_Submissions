# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.maxLength = -inf
        self.search(root,1)
        return self.maxLength

    def search(self, root, depth):
        if root.left == None and root.right == None:
            self.maxLength = max(self.maxLength, depth)
            return
        if root.left:
            self.search(root.left,depth + 1)
        if root.right:
            self.search(root.right, depth + 1)