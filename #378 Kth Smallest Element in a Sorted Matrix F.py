#378. Kth Smallest Element in a Sorted Matrix 
(I think I need to use heap to solve it later...to be continued...)

#1 (98s)
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        mlist=[]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix)):
                mlist.append(matrix[i][j])
        
        mlist.sort()
        return mlist[k-1]
            
