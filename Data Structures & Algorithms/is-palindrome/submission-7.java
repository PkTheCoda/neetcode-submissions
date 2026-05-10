class Solution {
    public boolean isPalindrome(String s) {
        String total = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (total.indexOf(s.charAt(left)) < 0 || total.indexOf(s.charAt(right)) < 0) {
                if (total.indexOf(s.charAt(left)) == -1) {
                    left++;
                }
                if (total.indexOf(s.charAt(right)) == -1) {
                    right--;
                }
            } else if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            } else {
                left++;
                right--;
            }
        }
        return true;
    }
}
