# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
            if not root:
                return 0
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #for every node, find the max depth of its left and right tree
        #and check if their difference < 2        

        if not root:
            return True
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        if abs(left_depth - right_depth) < 2:
            # Check recursively for every node
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        
         
         

        
