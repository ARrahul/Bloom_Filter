import random
def murmur(w):
    word = w
    c1 = int(0xcc9e2d51)
    c2 = int(0x1b873593)
    m = int(0x5)
    n = int(0xe6546b64)
    seed = 123
    Hash = seed

    if (len(word) >= 4) and (len(word) < 8):
        word1 = []
        word1 = word[:4]
        b = 24
        k = 0
        for i in range(len(word1)):
            a = ord(word1[i].lower())
            a = (a << b)
            b -= 8
            k = (k + a)
        # print (hex(k))
        k *= c1
        k = k << 15
        k *= c2
        Hash = Hash ^ k
        Hash = Hash << 13
        Hash = (Hash * m) + n
        # print (hex(Hash))

        leftover = []
        leftover = word[4:]
        b = 16
        k2 = 0
        for i in range(len(leftover)):
            a = ord(leftover[i].lower())
            a = a << b
            b -= 8
            k2 += a
        # print (k,k2)
        k2 *= c1
        k2 << 15
        k2 *= c2
        Hash = Hash ^ k2

        Hash = Hash ^ (len(word))
        # print (Hash)
        Hash ^= (Hash >> 16)
        Hash *= int(0x85ebca6b)
        Hash ^= (Hash >> 13)
        Hash *= int(0xc2b2ae35)
        Hash ^= (Hash >> 16)
        # Hash=Hash%LENNY
        return (Hash)
    if len(word) < 4:
        leftover = []
        leftover = word[0:]
        b = 16
        k2 = 0
        for i in range(len(leftover)):
            a = ord(leftover[i].lower())
            a = a << b
            b -= 8
            k2 += a
        # print (k,k2)
        k2 *= c1
        k2 << 15
        k2 *= c2
        Hash = Hash ^ k2

        Hash = Hash ^ (len(word))
        # print (Hash)
        Hash ^= (Hash >> 16)
        Hash *= int(0x85ebca6b)
        Hash ^= (Hash >> 13)
        Hash *= int(0xc2b2ae35)
        Hash ^= (Hash >> 16)
        # Hash=Hash%LENNY
        return (Hash)

    if len(word) >= 8 and len(word) < 12:
        word1 = []
        word1 = word[:4]
        b = 24
        k = 0
        for i in range(len(word1)):
            a = ord(word1[i].lower())
            a = (a << b)
            b -= 8
            k = (k + a)
        # print (hex(k))
        k *= c1
        k = k << 15
        k *= c2
        Hash = Hash ^ k
        Hash = Hash << 13
        Hash = (Hash * m) + n
        # print (hex(Hash))

        word2 = []
        word2 = word[4:8]
        b = 24
        k3 = 0
        for i in range(len(word2)):
            a = ord(word2[i].lower())
            a = (a << b)
            b -= 8
            k3 = (k3 + a)
        # print (hex(k))
        k3 *= c1
        k3 = k3 << 15
        k3 *= c2
        Hash = Hash ^ k3
        Hash = Hash << 13
        Hash = (Hash * m) + n

        leftover = []
        leftover = word[8:]
        b = 16
        k2 = 0
        for i in range(len(leftover)):
            a = ord(leftover[i].lower())
            a = a << b
            b -= 8
            k2 += a
        # print (k,k2)
        k2 *= c1
        k2 << 15
        k2 *= c2
        Hash = Hash ^ k2

        Hash = Hash ^ (len(word))
        # print (Hash)
        Hash ^= (Hash >> 16)
        Hash *= int(0x85ebca6b)
        Hash ^= (Hash >> 13)
        Hash *= int(0xc2b2ae35)
        Hash ^= (Hash >> 16)
        # Hash=Hash%LENNY
        return (Hash)
    if len(word) >= 12 and len(word) < 16:
        word1 = []
        word1 = word[:4]
        b = 24
        k = 0
        for i in range(len(word1)):
            a = ord(word1[i].lower())
            a = (a << b)
            b -= 8
            k = (k + a)
        # print (hex(k))
        k *= c1
        k = k << 15
        k *= c2
        Hash = Hash ^ k
        Hash = Hash << 13
        Hash = (Hash * m) + n
        # print (hex(Hash))

        word2 = []
        word2 = word[4:8]
        b = 24
        k3 = 0
        for i in range(len(word2)):
            a = ord(word2[i].lower())
            a = (a << b)
            b -= 8
            k3 = (k3 + a)
        # print (hex(k))
        k3 *= c1
        k3 = k3 << 15
        k3 *= c2
        Hash = Hash ^ k3
        Hash = Hash << 13
        Hash = (Hash * m) + n

        word3 = []
        word3 = word[8:12]
        b = 24
        k = 0
        for i in range(len(word3)):
            a = ord(word3[i].lower())
            a = (a << b)
            b -= 8
            k = (k + a)
        # print (hex(k))
        k *= c1
        k = k << 15
        k *= c2
        Hash = Hash ^ k
        Hash = Hash << 13
        Hash = (Hash * m) + n

        leftover = []
        leftover = word[12:]
        b = 16
        k2 = 0
        for i in range(len(leftover)):
            a = ord(leftover[i].lower())
            a = a << b
            b -= 8
            k2 += a
        # print (k,k2)
        k2 *= c1
        k2 << 15
        k2 *= c2
        Hash = Hash ^ k2

        Hash = Hash ^ (len(word))
        # print (Hash)
        Hash ^= (Hash >> 16)
        Hash *= int(0x85ebca6b)
        Hash ^= (Hash >> 13)
        Hash *= int(0xc2b2ae35)
        Hash ^= (Hash >> 16)
        # Hash=Hash%LENNY
        return (Hash)
    return 0


class node:
    def __init__(self):
        self.l=[]


class cuckoo:
    def fingerprint(self,x):
        a=str(x)
        a=murmur(a)
        a=a%1000
        return a

    def hash(self,x):
        x=str(x)
        a=murmur(x) % self.size
        return a

    def __init__(self,size):
        self.size=size
        self.array=[None] * self.size
        self.nb=4
        self.MaxNoofKiks=50
        for i in range(len(self.array)):
            self.array[i]=node()




    def insert(self,strg):
        strings=str(strg)
        f=self.fingerprint(str(strg))
        i=self.hash(str(strg))
        j = (i ^ self.hash(f)) % self.size
        if len(self.array[i].l)<self.nb or len(self.array[j].l)<self.nb:
            r=random.randint(1,2)
            if len(self.array[i].l) < self.nb and len(self.array[j].l) < self.nb:
                if r==1:
                    self.array[i].l.append(f)
                else:
                    self.array[j].l.append(f)
            else:
                if len(self.array[i].l)<self.nb:
                    self.array[i].l.append(f)

                else:
                    self.array[j].l.append(f)

            return True
        r=random.randint(1,2)
        if r==1:
            i=i
        else:
            i=j
        for n in range(self.MaxNoofKiks):
            fnew=f
            rs=random.randint(0, 3)
            f=self.array[i].l[rs]
            self.array[i].l[rs]=fnew
            i = (i ^ self.hash(f)) % self.size
            if len(self.array[i].l)<self.nb:
                self.array[i].l.append(f)
                return True
        self.delete(strings)
        print ("insertion fails")
        self.secondinsert(f,i)
        return False


    def secondinsert(self,f,i):
        j = (i ^ self.hash(f)) % self.size
        if len(self.array[i].l) < self.nb or len(self.array[j].l) < self.nb:
            r = random.randint(1, 3)
            if len(self.array[i].l) < self.nb and len(self.array[j].l) < self.nb:
                if r == 1:
                    self.array[i].l.append(f)
                else:
                    self.array[j].l.append(f)
            else:
                if len(self.array[i].l) < self.nb:
                    self.array[i].l.append(f)

                else:
                    self.array[j].l.append(f)

            return True
        r = random.randint(1, 2)
        if r == 1:
            i = i
        else:
            i = j
        for n in range(self.MaxNoofKiks):
            fnew = f
            rs = random.randint(0, 3)
            f = self.array[i].l[rs]
            self.array[i].l[rs] = fnew
            i = (i ^ self.hash(f)) % self.size
            if len(self.array[i].l) < self.nb:
                self.array[i].l.append(f)
                s=2
                return True
            print ("i am going infinity")
        return False

    def search(self,x):
        f=self.fingerprint(x)
        i=self.hash(x)
        j = (i ^ self.hash(f)) % self.size
        if f in self.array[i].l:
            return True
        if f in self.array[j].l:
            return True
        return False


    def delete(self,x):
        f = self.fingerprint(x)
        i = self.hash(x)
        j = (i ^ self.hash(f)) % self.size
        if f in self.array[i].l:
            self.array[i].l.remove(f)
            return True
        if f in self.array[j].l:
            self.array[j].l.remove(f)
            return True
        return False
  


  




o=cuckoo(3)
x=0
g=0
L=["RAHUL","MAHESH","HELLO","MANOJ","REKHA"]
for i in range(len(L)):
    o.insert(L[i])
for i in range(len(L)-2):
    o.delete(L[i])

print (o.search("MAHESH"))


