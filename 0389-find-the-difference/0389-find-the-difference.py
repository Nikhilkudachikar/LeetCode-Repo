from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_freq = Counter(s)
        t_freq = Counter(t)
        for k,v in t_freq.items():
            if k not in s_freq:
                return k
            elif s_freq[k] != v:
                return k