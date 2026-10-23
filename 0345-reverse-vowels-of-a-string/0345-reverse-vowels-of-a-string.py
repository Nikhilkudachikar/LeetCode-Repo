class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[]
        ind=[]
        c1=0
        a1=[]
        for i in s:
            a1.append(i)
            if i in "aeiou" or i in "AEIOU":
                ind.append(c1)
                vowels.append(i)
            c1+=1
        vowels.reverse()
        c=0
        for i in ind:
            a1[i]=vowels[c]
            c+=1
        return "".join(a1)