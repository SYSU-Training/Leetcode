129. Sum Root to Leaf Numbers 
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        num=[]
        if not root:
            return 0
        def path_num(root,path):
            if not root.left and not root.right:
                num.append(path)
            if root.left:
                path_num(root.left,path+str(root.left.val))
            if root.right:
                path_num(root.right,path+str(root.right.val))
        path_num(root,str(root.val))
        number=[int(i) for i in num]
        return sum(number)