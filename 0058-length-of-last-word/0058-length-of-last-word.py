class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1=s.strip()
        s2=s1.split()
        w=s2[-1]
        return len(w)
        