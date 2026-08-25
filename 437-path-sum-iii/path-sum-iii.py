# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case: path starting directly from the root

        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val
            # Number of valid sub-paths ending at the current node
            count = prefix_sums[current_sum - targetSum]

            # Add current prefix sum to map for child nodes
            prefix_sums[current_sum] += 1

            # Traverse left and right children
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            # Backtrack: remove current sum so it doesn't spill into parallel branches
            prefix_sums[current_sum] -= 1

            return count

        return dfs(root, 0)