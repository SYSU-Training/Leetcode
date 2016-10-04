class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n=matrix.size();
        int min=matrix[0][0],max=matrix[n-1][n-1];
		while (min<max) {
			int mid=(max+min)/2;
			int i=n-1,j=0,m=0;
			while (i>=0&&j<n) 
			{
			    if(matrix[i][j]<=mid) 
			    {
			        j++;
			        m=m+i+1;
			    }
			else i--;
			}
			if(m<k) min=mid+1;
			else max=mid;
		}
		return min;
	}
};
