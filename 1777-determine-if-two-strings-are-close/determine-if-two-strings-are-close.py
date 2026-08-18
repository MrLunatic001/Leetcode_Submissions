class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1, w2 = defaultdict(int), defaultdict(int)

        for word in word1:
            w1[word] += 1
        for word in word2:
            w2[word] += 1

        if set(w1.keys()) == set(w2.keys()) and sorted(w1.values()) == sorted(w2.values()):
            return True
        return False