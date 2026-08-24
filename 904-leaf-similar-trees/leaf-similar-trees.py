# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.leaf1 = []
        self.leaf2 = []
        self.search(root1,1)
        self.search(root2,2)

        return self.leaf1 == self.leaf2

    def search(self, root, leaf):
        if not root:
            return
        if not root.left and not root.right:
            if leaf == 1:
                self.leaf1.append(root.val)
                return
            else:
                self.leaf2.append(root.val)
                return
        if root.left:
            self.search(root.left, leaf)

        if root.right:
            self.search(root.right, leaf)