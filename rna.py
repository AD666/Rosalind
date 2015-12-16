s=str(input())
a=0
for i in range (0,len(s)):
    if s[i]=="T" :
        s=s.replace("T","U")
print (s)
