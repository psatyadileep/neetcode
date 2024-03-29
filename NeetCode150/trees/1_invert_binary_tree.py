"""
LC226: Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return None


        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
