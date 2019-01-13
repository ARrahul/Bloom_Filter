import fnv
import mmh3
name=input("Enter Your Name :")
dat=input("Enter Your Date Of Birth(ddmmyyyy) :")
LENNY=35677
a=mmh3.murmur(name)
b=fnv.fnv(name)
c=mmh3.murmur(dat)
d=fnv.fnv(dat)

a=a%LENNY
b=b%LENNY
c=c%LENNY
d=d%LENNY

m=[None for i in range(LENNY)]
m[a]=m[b]=m[c]=m[d]=1
with open("10k.txt") as dict:
    dict1 = dict.read().split('\n')


for i in range(len(dict1)):
    a=[]
    a=dict1[i]
    n=mmh3.murmur(a)
    f=fnv.fnv(a)
    n=n%LENNY   
    f=f%LENNY
    m[n]=1
    m[f]=1
x=2
pas=input("Enter a password :")
e=mmh3.murmur(pas)
e=e%LENNY
f=fnv.fnv(pas)
f=f%LENNY
if m[e]==1 and m[f]==1:
    x=1

while x==1:
    pas=input("Oops ! Enter new password :")
    e=mmh3.murmur(pas)
    e=e%LENNY
    f=fnv.fnv(pas)
    f=f%LENNY
    if m[e]==1 and m[f]==1:
        x=1
    elif m[e]==None or m[f]==None:
        x=2
print ("Password has successfully been changed")    


   ##password checking case for lower,upper and number 


    
    
    


        
           

