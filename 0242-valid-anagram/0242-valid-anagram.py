class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for i in t:
            s=s.replace(i,"",1)
        if s=="":
            return True
        else:
            return False