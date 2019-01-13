import math
import prime
import fnv
import mmh3
import horner
x=input("Enter the filename of the first database :")
y=input("Enter the filename of the second database :")

with open(x) as dict :
    dict1 = dict.read().split('\n')
with open(y) as dict :
    dict2 = dict.read().split('\n')
if len(dict1)<len(dict2):
    n=len(dict2)
else:
    n=len(dict1)
p=0.18
m1=((float(n)*float(math.log(p)))/float(math.log(1.0/(math.pow(2,float(math.log(2)))))))
k=(float(math.log(2))*float(m1)/float(n))
#print (math.floor(m),math.floor(k))
LENNY=prime.prime(math.ceil(m1))
m=[None for i in range(LENNY)]
if len(dict1)>len(dict2):
    for i in range(len(dict1)):
        a=[]
        a=dict1[i]
        n=mmh3.murmur(a.lower())
        n=n%LENNY
        f=fnv.fnv(a.lower())
        f=f%LENNY
        q=horner.hash3(a.lower())
        q=q%LENNY
        m[n]=1
        m[f]=1
        m[q]=1
    def search():
        t=0
        e=0
        for i in range(len(dict2)):
            x=dict2[i]
            q=x
            b=mmh3.murmur(q.lower())
            b=b%LENNY
            w=fnv.fnv(q.lower())
            w=w%LENNY
            g=horner.hash3(q.lower())
            g=g%LENNY
        
            if m[b]==1 and m[w]==1 and m[g]==1:
                t=t+1
            elif m[b]==None or m[w]==None or m[g]==None:
                e=e+1
        print ("Number of common elements are(aprox)",t) 
    search()
else:
    for i in range(len(dict2)):
        a=[]
        a=dict2[i]
        n=mmh3.murmur(a.lower())
        n=n%LENNY
        f=fnv.fnv(a.lower())
        f=f%LENNY
        q=horner.hash3(a.lower())
        q=q%LENNY
        m[n]=1
        m[f]=1
    def search():
        t=0
        e=0
        for i in range(len(dict1)):
            x=dict1[i]
            q=x
            b=mmh3.murmur(q.lower())
            b=b%LENNY
            w=fnv.fnv(q.lower())
            w=w%LENNY
            g=horner.hash3(q.lower())
            g=g%LENNY
        
            if m[b]==1 and m[w]==1 and m[g]==1:
                t=t+1
            elif m[b]==None or m[w]==None or m[g]==None:
                e=e+1
        print ("Number of common elements are(approx)",t) 
    search()

