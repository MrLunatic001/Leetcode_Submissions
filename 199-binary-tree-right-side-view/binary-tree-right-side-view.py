# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque()
        q.append((root,1))
        level = 0
        if not root:
            return []
        rightMost = root
        while q:
            item = q.popleft()
            if level < item[1]:
                ans.append(rightMost.val)
                rightMost = None
            level = item[1]
            n = item[0]
            if not rightMost:
                rightMost = n

            if n.left:
                rightMost = n.left
                q.append((n.left,level+1))
            if n.right:
                rightMost = n.right
                q.append((n.right,level+1))

            


        return ans

        