#111. Minimum Depth of Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth=[]
        if root==None:
            return 0
        def dfs(root,d):
            if not root.left and not root.right:
                depth.append(d)
            if root.left:
                dfs(root.left,d+1)
            if root.right:
                dfs(root.right,d+1)
        dfs(root,1)
        return min(depth)