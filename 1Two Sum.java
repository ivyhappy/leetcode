public class Solution {
    public int[] twoSum(int[] nums, int target) {
      //10ms 
      //using map.containsKey will be 12ms, and there is some method faster. Figure it out later.
        int length = nums.length;
        if(length<=1){
            return new int[2];
        }
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();   
        for (int i=0;i<length;i++){
            if(map.get(target-nums[i]) != null){
                //System.out.println("222:"+i);
                return new int[] {map.get(target-nums[i]),i};
            }
            else{
                //System.out.println(i);
                map.put(nums[i],i);
            }
        }
        return new int[2];
    }
}
