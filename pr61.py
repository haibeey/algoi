def cyclic(guys):
    #to check if a set of number satifies the cyclic property
    for i in range(len(guys)):
        k=0
        b=[0,0]
        for j in range(len(guys)):
            if i!=j:
                if str(guys[i])[:2]==str(guys[j])[2:] and not b[0]:
                    k+=1;b[0]=1
                elif str(guys[i])[2:]==str(guys[j])[:2] and not b[1]:
                    k+=1;b[1]=1
        if k<2:
            return False
    return True

def v(a,b):
    return str(a)[2:]==str(b)[:2]
def tri(n):
    return int((n*(n+1))/2)

def sq(n):
    return n*n

def pen(n):
    return int((n*((3*n)-1))/2)

def hex(n):
    return n*((2*n)-1)

def hep(n):
    return int((n*((5*n)-3))/2)

def oct(n):
    return int(n*((3*n)-2))

funcs=[(sq,31,100),(pen,26,82),(hex,23,71),(hep,21,64),(oct,19,59)]
def getanywithpre(pre,chosen):
    res=[]
    if 4 not in chosen:
        for i in [sq(i) for i in range(31,100)]:
            if pre==str(i)[:2]:
                res.append((i,4))
    if 5 not in chosen:
        for i in [pen(i) for i in range(26,82)]:
            if pre==str(i)[:2]:
                res.append((i,5))
    if 6 not in chosen:
        for i in [hex(i) for i in range(23,71)]:
            if pre==str(i)[:2]:
                res.append((i,6))
    if 7 not in chosen:
        for i in [hep(i) for i in range(21,64)]:
            if pre==str(i)[:2]:
                res.append((i,7))
    if 8 not in chosen:
        for i in [oct(i) for i in range(19,59)]:
            if pre==str(i)[:2]:
                res.append((i,8))
    return res

def sp(res,Next,chosen):
    global funcs
    if Next==6:
        return 0
    if len(res)==6 and v(res[-1],res[0]):
        print(sum(res))
        print(cyclic(res))
        return res
    else:
        for i in getanywithpre(str(res[-1])[2:],chosen):
            if v(res[-1],i[0]):
                (sp(res+[i[0]],Next+1,chosen+[i[1]]))
import time
timeStart=time.time()
for i in range(45,141):
    sp([tri(i)],0,[3])
print(time.time()-timeStart)
#runs in 0.5 plus secss
    
