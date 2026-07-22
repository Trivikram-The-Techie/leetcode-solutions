# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], curr: int) -> int:
            if not node:
                return 0
            
            # Shift bits left by 1 and include current node's value
            curr = (curr << 1) | node.val
            
            # If it's a leaf node, return the binary value of the path
            if not node.left and not node.right:
                return curr
            
            # Sum up paths from both subtrees
            return dfs(node.left, curr) + dfs(node.right, curr)
        
        return dfs(root, 0)
        