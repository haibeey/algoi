
class myDict(dict):
    """i Needed to add some functionalties to the dict class"""
    def __getitem__(self,x):
        "might cause memory leakage though"
        if not self.__contains__(x):
            self.__setitem__(x,[])
        return super().__getitem__(x)
    
def sortAndGet(value,u):
    value=[int(i) for i in str(value)]
    a=[0]*10
    for i in value:
        a[i]+=1
    b=[0]*10
    b[0]=a[0]
    for i in range(1,10):
        b[i]=a[i]+b[i-1]
    res=[0]*30
    for i in value:
        res[b[i]]=i
        b[i]-=1
    res=[str(i) for i in res if i]
    return int(''.join(res)),u



HASH=myDict()
for i in range(300,40100):#fortunately ans was in this range
    res=sortAndGet(i**3,i)
    here=HASH[res[0]]
    if not len(here):
        HASH[res[0]].append(res[1])
    else:
        if len(str(HASH[res[0]][0]**3))==len(str(res[1]**3)):
            HASH[res[0]].append(res[1])
res=11111111111111111111111111
for i in HASH:
    if len(HASH[i])==5:
        res=min(res,min(HASH[i]))

print(res**3)
