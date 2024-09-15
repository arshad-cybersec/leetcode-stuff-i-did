class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}

        lastSeenIndex = {0:-1,}

        n = len(s)
        maxLen, mask = 0, 0
        for i in range(n):
            if s[i] in "aeiou":
                mask ^= vowels[s[i]]
            if mask in lastSeenIndex:
                maxLen = max(maxLen, i -lastSeenIndex[mask])
            else:
                lastSeenIndex[mask] = i
        return maxLen