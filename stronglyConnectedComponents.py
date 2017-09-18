from collections import deque #WTF i could have just use a list

#making this global is bad?
#This should fine,except when multithreadind (><)
stack=deque()
clock=0
vis=[0]*10
graph=[]

def DFS1(v):
    '''This is for dfs on a adjacency matrix graph'''
    global vis
    vis[v]=1
    components=[v]
    for i in range(len(graph[0])):
        if graph[v][i]:
            if not vis[i]:
                components+=DFS1(i)
    return components
    
def DFS2(v):
    '''This is for dfs on a adjacency list graph'''
    global vis
    vis[v]=1
    components=[]
    components.append(v)
    for i in graph[v]:
        if not vis[i]:
            components+=DFS2(i)
    return components

def reverseAMatrixGraph(graph):
    def dfs(v):
        vis[v]=1
        for i in range(len(graph[0])):
            if graph[v][i]:
                ngraph[i][v]=1
            if graph[v][i] and not vis[i]:
                ngraph[i][v]=1
                dfs(i)
    ngraph=[[0]*len(graph[0]) for i in range(len(graph))]
    vis=[0]*len(graph)
    for i in range(len(graph)):
        if not vis[i]:
            dfs(i)
    return ngraph

def reverseAgraph(graph):
    def dfs(v):
        vis[v]=1
        for i in graph[v]:
            ngraph[i].append(v)
            if not vis[i]:
                dfs(i)
    ngraph={i:[] for i in graph}
    vis=[0]*len(graph)
    for i in range(len(graph)):
        if not vis[i]:
            dfs(i)
    return ngraph

def SCC4undirectedgraph1(graph):
    ''' for adjacency matrix like graph'''
    global vis
    allComponents=[]
    vis=[0]*len(graph)
    for i in range(len(graph[0])):
        if not vis[i]:
            allComponents.append(DFS1(i))
    return allComponents

def SCC4undirectedgraph2(graph):
    ''' for  a adjacency list like graph'''
    global vis
    allComponents=[]
    vis=[0]*len(graph)
    for i in range(len(graph[0])):
        if not vis[i]:
            allComponents.append(DFS2(i))
    return allComponents

def SCC4directedGraph1(graph):
    '''gets SCC for graph of in matrix form'''
    reversedGraph=reverseAgraph(graph)
    time=[0]*len(graph)
    vis=[0]*len(graph)
    def dfs(v):
        global clock,stack
        vis[v]=1
        for i in reversedGraph[v]:
            if not vis[i]:
                dfs(i)
        if v in stack:return
        time[v]=clock+1
        clock+=1
        stack.append(v)
    def dfs1(v):
        global stack
        vis[v]=1
        stack.remove(v)
        component=[v]
        for i in graph[v]:
            if not vis[i]:
                component+=dfs1(i)
        return component
    vis=[0]*len(graph)
    for i in range(len(graph)):
        dfs(i)
    vis=[0]*len(graph)
    SCC=[]
    while stack:
        curVertex=stack.pop()
        stack.append(curVertex)
        SCC.append(dfs1(curVertex))
    return SCC

def SCC4directedGraph2(graph):
    '''gets SCC for a graph'''
    reversedGraph=reverseAMatrixGraph(graph)
    time=[0]*len(graph)
    vis=[0]*len(graph)
    def dfs(v):
        global clock,stack
        vis[v]=1
        for i in range(len(graph[0])):
            if reversedGraph[v][i] and not vis[i]:
                dfs(i)
        if v in stack:return
        time[v]=clock+1
        clock+=1
        stack.append(v)
    def dfs1(v):
        global stack
        vis[v]=1
        stack.remove(v)
        component=[v]
        for i in range(len(graph[v])):
            if graph[v][i] and not vis[i]:
                component+=dfs1(i)
        return component
    vis=[0]*len(graph)
    for i in range(len(graph)):
        dfs(i)
    vis=[0]*len(graph)
    SCC=[]
    while stack:
        curVertex=stack.pop()
        stack.append(curVertex)
        SCC.append(dfs1(curVertex))
    return SCC
    
def readInput(Type):
    #This function read input. Should be overidden
    global stack,clock,vis,graph
    stack=deque()
    clock=0
    if Type[0]=='a':
        with open('test.txt','r') as file:
            m,n=map(int,file.readline().split())
            graph=[[0]*m for i in range(m)]
            for i in range(n):
                a,b=map(int,file.readline().split())
                graph[a][b]=1
            vis=[0]*m
            print(SCC4undirectedgraph1(graph))
            return graph
    elif Type[0]=='m':
        with open('test.txt','r') as file:
            n,m=map(int,file.readline().split())
            graph={i:[] for i in range(n)}
            for i in range(m):
                a,b=map(int,file.readline().split())
                graph[a].append(b)
            vis=[0]*n
            print(SCC4undirectedgraph2(graph))
            return graph
    else:
        raise Exception


'''
readinput takes argument of type of graph (a,b) and return the appropriate type.

SCC4directedGraph1 take a adjacency list type graph and spit out connected components for directed graphs.

SCC4directedGraph1 take a adjacency list type graph and spit out connected components for directed graphs.

SCC4undirectedgraph1 take a adjacency matrix type graph and spit out connected components for undirected graphs

SCC4undirectedgraph2 take a adjacency list type graph and spit out connected components for undirected graphs
'''

