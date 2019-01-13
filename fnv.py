def fnv(strings):
    s=strings
    fnvprime=16777619
    hash=2166136261
    for i in range(len(s)):
        charcode = int(ord(strings[i]))
        firstoctet = (charcode & 0xFF)
        hash = hash ^ firstoctet
        hash = (hash * fnvprime)|0
        secondoctet = (charcode >> 8)
        hash = hash ^ secondoctet
        hash = (hash * fnvprime) | 0
    
    return hash


