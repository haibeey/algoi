from math import log
ans=0
for i in range(1,50):
    for j in range(1,2**32):
        if len(str(j**i))==i:
            ans+=1
        if len(str(j**i))>i:
            #print(j**i)
            break

print(ans)
