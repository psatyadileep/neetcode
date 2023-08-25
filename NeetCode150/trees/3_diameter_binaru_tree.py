"""
LC543: Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_dia = 0
        left_tree = 1+self.diameterOfBinaryTree(root.left)
        right_tree = 1+ self.diameterOfBinaryTree(root.right)
        max_dia = max(max_dia,left_tree+right_tree)


        return max_dia




