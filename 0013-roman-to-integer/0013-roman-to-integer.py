class Solution:
    def romanToInt(self, s: str) -> int:
        rom_set={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900,'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=0
        while s:
            for k,v in rom_set.items():
                if k in s:
                    res+=v
                    s=s.replace(k,"",1)
        return res
s=Solution()
print(s.romanToInt("III"))
