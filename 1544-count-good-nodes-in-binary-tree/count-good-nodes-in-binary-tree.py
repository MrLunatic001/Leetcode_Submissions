# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 0
        self.search(root, root.val)

        return self.counter

    def search(self, root, currentMaxVal):
        if root.val >= currentMaxVal:
            self.counter += 1
            currentMaxVal = root.val
        if not root.left and not root.right:
            return
        if root.left:
            self.search(root.left, currentMaxVal)
        if root.right:
            self.search(root.right, currentMaxVal)

