class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alb="abcdefghijklmnopqrstuvwxyz"
        for i in alb:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True



        