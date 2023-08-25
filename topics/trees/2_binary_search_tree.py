"""

LC200: https://leetcode.com/problems/search-in-a-binary-search-tree/
Every single node in left subtree is less than the node above
every nod ein the right subtree is greater the the node above
"""


def search(root, target):

    if not root:
        return False


    if target>root.value:
        return search(root.right,target)

    elif target<root.value:
        return  search(root.left,target)

    else:
        return True

"""
Time complexity = Log(n) if its balanced 
"""