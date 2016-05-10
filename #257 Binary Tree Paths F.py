#257. Binary Tree Paths
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
   
    def binaryTreePaths(self, root):
        result=[]
        if root==None:
            return result
        def dfs(root, path):
    		if root.right==None and root.left==None:
    			result.append(path)
    		if root.right:
    			dfs(root.right, path+'->'+str(root.right.val))
    		if root.left:
    			dfs(root.left, path+'->'+str(root.left.val))
        dfs(root,str(root.val))
        return result

#Test Tree
root=TreeNode(3)
a1=TreeNode(5)
a1.right=TreeNode(1)
a1.left=TreeNode(2)
root.left=a1
root.right=TreeNode(10)
 
 #	 	 3
 #		/ \
 #	   5  10
 # 	  /\
 # 	 2  1
 
 #Testing
obj=Solution()
results=obj.binaryTreePaths(root)
print results