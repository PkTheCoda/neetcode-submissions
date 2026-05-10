class Solution {
    public boolean hasDuplicate(int[] nums) {

        HashSet<Integer> passed = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (passed.contains(nums[i])) {
                return true;
            }
            passed.add(nums[i]);
        }

        return false;
    }
}