num=int(input())
temp=num
count=0
first=last=0
digit=0
new=0
p=1
while num:
    r=num%10
    num=num//10
    count+=1
digit=count=count-1
num=temp
if num>0:
    first=num//pow(10,count)
    last=num%10
while num:
    r=num%10
    num=num//10
    if count==digit:
        r=first
    elif count==0:
        r=last
    new=new+r*p
    p=p*10
    count-=1
print(new)    
    
