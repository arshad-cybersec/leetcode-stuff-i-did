class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_words = s1.split(' ')
        s2_words = s2.split(' ')
        total_words = s1_words + s2_words
        count = Counter(total_words)

        return [word for word in count if count[word] == 1]