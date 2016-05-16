#Validate Binary Search Tree 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  # @param root, a tree node
  # @return a boolean
  def isValidBST(self, root):
    return self._isValidBST(root,-float('inf') , float('inf'));

  def _isValidBST(self, root, min, max):
    if root is None or root.val is None:
      return True
	return root.val < max and root.val > min and self._isValidBST(root.left, min, root.val) and self._isValidBST(root.right, root.val, max)

# Question: About "self" in "function" and "class" ?