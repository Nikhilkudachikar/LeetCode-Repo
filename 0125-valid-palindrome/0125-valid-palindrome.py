class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s.lower().strip()
        s2=""
        for i in range(len(s1)):
            if s1[i].isalnum():
                s2=s2+s1[i]
        if s2==s2[::-1]:
            return True
        else:
            return False
