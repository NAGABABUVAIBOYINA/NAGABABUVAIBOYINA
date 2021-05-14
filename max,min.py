num=int(input())
ma=num%10
mi=num%10
c=0
d=0
while num:
    r=num%10
    num=num//10
    if r>ma:
        ma=r
        c=1
    elif ma==r:
        c+=1
    if r<mi:
        mi=r
        d=1
    elif mi==r:
        d+=1
print(ma,mi,c,d)        
        
