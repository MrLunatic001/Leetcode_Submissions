# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_sum = float('-inf')
        best_level = 1
        current_level = 1
        
        q = deque([root])
        
        while q:
            level_sum = 0
            # Process all nodes in the current level
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Check if current level has a strictly greater sum
            if level_sum > max_sum:
                max_sum = level_sum
                best_level = current_level
                
            current_level += 1
            
        return best_level

