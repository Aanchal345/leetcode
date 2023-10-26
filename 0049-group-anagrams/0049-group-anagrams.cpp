class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
            vector<vector<string>>ans;
        unordered_map<string,vector<string>>umap;
        for(auto X : strs){
            string temp = X;
            sort(X.begin(), X.end());
            umap[X].push_back(temp);
            
        }
            for(auto X : umap){
                ans.push_back(X.second);    
    }
        return ans;
    }
};