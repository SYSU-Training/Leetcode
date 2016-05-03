class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector< vector<int> > result;  
        if (numRows<= 0)  return result;  
        for(int i=1; i<=numRows; i++){  
            vector<int> *test = new vector<int>();  
            test->push_back(1);  
            if (i == 1)  
            {
                result.push_back(*test);
                continue;
            }
            vector<int> last = result[i-2];
            for (int j = 0; j <i-2; j++)
            {
                test->push_back(last[j]+last[j+1]);
            }
            test->push_back(1);
            result.push_back(*test);
        }
        return result;
    }
};
