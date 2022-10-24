# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # use dfs to traverse through binary tree to the leaf node
        # need something to keep track of sum throughout each level
        # if sum == targetSum return True
        # else return False
        # use dfs
        
        if not root:
            return False
        
        if not root.right and not root.left:
            return root.val == targetSum
        
        return self.hasPathSum(root.right, targetSum - root.val) or self.hasPathSum(root.left, targetSum - root.val)
            