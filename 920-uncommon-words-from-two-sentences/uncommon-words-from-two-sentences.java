class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        Map<String, Integer> map = new HashMap<>();
        String[] str1 = s1.split(" ");
        String[] str2 = s2.split(" ");
        for (String word : str1) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        for (String word : str2) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        ArrayList<String> ans = new ArrayList<>();
        for (Map.Entry<String, Integer> mp : map.entrySet()) {
            if (mp.getValue() == 1) {
                ans.add(mp.getKey());
            }
        }

        return ans.toArray(new String[0]);

    }
}