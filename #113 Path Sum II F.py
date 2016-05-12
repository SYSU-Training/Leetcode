#113. Path Sum II
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result=[]
        if root==None:
            return result
        def path(root, path_list, add):
            if root.right==None and root.left==None:
                if add==sum:
                    result.append(path_list)
            if root.left:
                path(root.left, path_list+[root.left.val],add+root.left.val)
            if root.right:
                path(root.right, path_list+[root.right.val],add+root.right.val)
        path(root,[root.val],root.val)
        return result
                