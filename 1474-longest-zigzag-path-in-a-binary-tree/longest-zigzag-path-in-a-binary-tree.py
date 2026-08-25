# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def search(node, currentLength, direction):
            if not node:
                return

            # Update answer at every visited node, not just leaves
            self.ans = max(self.ans, currentLength)

            # Direction 0: previous step was to the Left (or starting point)
            if direction == 0:
                # Continue ZigZag to the Right (+1 step)
                search(node.right, currentLength + 1, 1)
                # Reset ZigZag path going to the Left (1 step start)
                search(node.left, 1, 0)

            # Direction 1: previous step was to the Right (or starting point)
            elif direction == 1:
                # Continue ZigZag to the Left (+1 step)
                search(node.left, currentLength + 1, 0)
                # Reset ZigZag path going to the Right (1 step start)
                search(node.right, 1, 1)

        # Start initial searches from root (0 edges so far)
        search(root, 0, 0)
        search(root, 0, 1)

        return self.ans