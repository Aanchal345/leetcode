class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int,int>mp;
        for(int i=0;i<nums.size();i++){
            mp[nums[i]]=1;
        }
        int ans=0;
        for(int i=0;i<nums.size();i++){
            if(mp.find(nums[i]-1)!=mp.end()){
                continue;
            }
            else{
                int c=1;
                int ce=nums[i]+1;
                while(mp.find(ce)!=mp.end()){
                    c++;
                    ce++;
                }
                ans=max(ans,c);
            }
        }
        return ans;
        
    }
};