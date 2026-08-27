# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def bs(root,val):
    if not root:
        return None
    if root.val == val:
        return root
    elif val > root.val:
        return bs(root.right,val)
    else:
        return bs(root.left,val)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return bs(root,val)
