import math
def hash3(str):
    x=41
    a=str
    sum=0
    for i in range(len(a)):
        sum+=pow(x,i)*ord(a[i])
    return (sum)
