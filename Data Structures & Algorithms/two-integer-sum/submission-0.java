class Solution {
    public int[] twoSum(int[] nums, int target) {
        // complement (target - currentNum), index
        HashMap<Integer, Integer> freqCount = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (freqCount.containsKey(target - nums[i])) {
                int[] toReturn = {freqCount.get(target - nums[i]), i};
                return toReturn;
            } else {
                freqCount.put(nums[i], i);
            }
        } 

        int[] random = {1,2};
        return random;
    }
}
