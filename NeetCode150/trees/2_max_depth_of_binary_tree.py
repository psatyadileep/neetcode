"""
LC104: Maximum depth of Binary tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the
 longest path from the root node down to the farthest leaf node.
"""

#Dfs solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



#Leve Order traversal
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        level = 1
        q = deque([root])

        while q:

            for i in range(len(q)):
                current = q.popleft()

                if current.left:
                    q.append(current.left)

                if current.right:
                    q.append(current.right)

            level+=1

        return root



