class Solution {
    public boolean hasDuplicate(int[] nums) {

        ArrayList<Integer> passed = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (passed.contains(nums[i])) {
                return true;
            } else {
                passed.add(nums[i]);
            }
        }

        return false;
    }
}