class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            Character currentChar = s.charAt(i);
            if (sMap.containsKey(currentChar)) {
                int currCount = sMap.get(currentChar);
                sMap.put(currentChar, currCount + 1);
            } else {
                sMap.put(currentChar, 1);
            }
        }

        for (int i = 0; i < t.length(); i++) {
            Character currentChar = t.charAt(i);
            if (tMap.containsKey(currentChar)) {
                int currCount = tMap.get(currentChar);
                tMap.put(currentChar, currCount + 1);
            } else {
                tMap.put(currentChar, 1);
            }
        }

        return sMap.equals(tMap);
    }
}
