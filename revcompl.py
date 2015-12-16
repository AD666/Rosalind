s=str(input())
a=0
a=s[::-1]
a=a.replace("T","t").replace("C","c").replace("A","T").replace("G","C").replace("t","A").replace("c","G")
print (a)
