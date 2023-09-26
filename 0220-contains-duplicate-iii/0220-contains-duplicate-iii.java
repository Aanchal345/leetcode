class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
         int j=0;
  for(int i=1;i<nums.length;i++)
  { 
      if(Math.abs(nums[i]-nums[j])<=valueDiff  && Math.abs(i-j)<=indexDiff)//check the condition;
      {
          return true;
      }
      else if(Math.abs(i-j)==indexDiff || i==nums.length-1)// condition to increase window size
          i=++j;
  }
 return false;
        
    }
}