#113 Path Sum II F.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#1?
class Solution(object):
	def hasPathSum(self, root, sum):
		if not root:
			return False
		if not root.left and not root.right:
	        return sum == root.val
	    return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


#2
class Solution(object):
    def hasPathSum(self, root, sum):

        result=[]
        if root==None:
            return False
        def path(root, path_list, add):
            if root.right==None and root.left==None:
                if add==sum:
                    result.append(path_list)
            if root.left:
                path(root.left, path_list+[root.left.val],add+root.left.val)
            if root.right:
                path(root.right, path_list+[root.right.val],add+root.right.val)
        path(root,[root.val],root.val)
        n=len(result)
        return True if n!=0 else False

