
class MinBinHeap(object):
    
    def __init__(self,a_list=None):
        if a_list:
            self.list=[0]+a_list
            self.min_heapify(a_list)
            self.len=len(a_list)
        else:
            self.list=[0]
            self.len=0

    def perc_up(self,i):
        while i/2>0:
            if self.list[i]<self.list[i/2]:
                self.list[i],self.list[i/2]=self.list[i/2],self.list[i]
            i/=2

    def insert(self,obj):
        self.list.append(obj)
        self.len+=1
        self.perc_up(self.len)
    
    def perc_down(self,i):
        while i*2<=self.len:
            mn=self.get_min_child(i)
            if self.list[i]>self.list[mn]:
                self.list[i],self.list[mn]=self.list[mn],self.list[i]
            i=mn

    def get_min_child(self,i):
        if i*2+1>self.len:
            return i*2
        elif self.list[i*2]<self.list[i*2+1]:
            return i*2
        else:
            return i*2+1

    def get_min(self):
        self.list[1],self.list[self.len]=self.list[self.len],self.list[1]
        result=self.list.pop()
        self.perc_down(1)
        self.len-=1
        return result
    
    def min_heapify(self,a_list):
        i=len(a_list)+1
        self.list=[0]+a_list[:]
        self.len=len(a_list)
        while i>0:
            self.perc_down(i)
            i-=1
        

class MaxBinHeap(object):
    def __init__(self,a_list=None):
        if a_list:
            self.list=[0]+a_list
            self.max_heapify(a_list)
            self.len=len(a_list)
        else:
            self.list=[0]
            self.len=0

    def perc_up(self,i):
        while i/2>0:
            if self.list[i]>self.list[i/2]:
                self.list[i],self.list[i/2]=self.list[i/2],self.list[i]
            i/=2

    def insert(self,obj):
        self.list.append(obj)
        self.len+=1
        self.perc_up(self.len)
    
    def perc_down(self,i):
        while i*2<=self.len:
            mn=self.get_max_child(i)
            if self.list[i]<self.list[mn]:
                self.list[i],self.list[mn]=self.list[mn],self.list[i]
            i=mn

    def get_max_child(self,i):
        if i*2+1>=self.len:
            return i*2
        elif self.list[i*2]<self.list[i*2+1]:
            return i*2+1
        else:
            return i*2

    def get_max(self):
        self.list[1],self.list[self.len]=self.list[self.len],self.list[1]
        result=self.list.pop()
        self.perc_down(1)
        self.len-=1
        return result
    
    def max_heapify(self,a_list):
        i=len(a_list)+1
        self.list=[0]+a_list[:]
        self.len=len(a_list)
        while i>0:
            self.perc_down(i)
            i-=1
        
"""
hp=MinBinHeap([9,10,1,4,0])
print(hp.list)
print(hp.get_min())
print(hp.list)
hp.insert(0)
print(hp.list)
print("------------------")
hp=MaxBinHeap([9,10,1,4,0])
print(hp.list)
print(hp.get_max())
print(hp.list)
hp.insert(0)
print(hp.list)
"""