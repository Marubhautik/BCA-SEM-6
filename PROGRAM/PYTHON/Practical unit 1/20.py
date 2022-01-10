def duplicate(li):
    n=len(li)
    dup=[]
    for i in range(n):
        k = i + 1
        for j in range(k,n):
            if li[i] == li[j] and li[i] not in dup:
                dup.append(li[i])
    return dup

#test
li=[ 10, 20, 30,-10, 10, 80, -10,30]
print("Duplicate integeres: ",duplicate(li))
