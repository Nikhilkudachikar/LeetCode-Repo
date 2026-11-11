class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s1=s.split("-")
        l=0
        s1_l=len(s1)
        for i in range(1,s1_l):
            l+=len(s1[i])
        if (s1_l==2 and s1[1]==""):
            rem= (l+len(s1[0]))%k
            s2="".join(s1).upper()
            g0=s2[:rem:]
            c=rem
            s3=""
            while c<len(s2):
                s3=s3+"-"+s2[c:c+k]
                c+=k
            s3=g0+s3
            return s3
            
        if (l+len(s1[0]))%k == 0:
            #g0=s1.pop(0)
            s2="".join(s1).upper()
            c=0
            s3=""
            while c<len(s2):
                s3=s3+"-"+s2[c:c+k]
                c+=k
            s3=s3[1::]
        elif l%k == 0:
            g0=s1.pop(0)
            s2="".join(s1).upper()
            c=0
            s3=""
            while c<len(s2):
                s3=s3+"-"+s2[c:c+k]
                c+=k
            s3=g0+s3
        else:
            rem= (l+len(s1[0]))%k
            s2="".join(s1).upper()
            g0=s2[:rem:]
            c=rem
            s3=""
            while c<len(s2):
                s3=s3+"-"+s2[c:c+k]
                c+=k
            s3=g0+s3
        
        
            
        return s3