import resource
import sys

resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
sys.setrecursionlimit(2 ** 17)

class Graph:
    
    def __init__(self, adj_lst):        
        self.graph = adj_lst  
    
    def addEdge(self, vertex1, vertex2): # add an edge from vertex1 to vertex2
        self.graph[vertex1].append(vertex2)
    
    def reverseGraph(self):        
        inverseG = Graph(defaultdict(list))
        
        for i in self.graph:
            for j in self.graph[i]:
                inverseG.addEdge(j, i)
        return inverseG

    def finishingTimeStack(self, vertex, visited, stack):
        
        visited[vertex] = True
        for i in self.graph[vertex]:
            if visited[i] == False:
                self.finishingTimeStack(i, visited, stack)
        stack.append(vertex)
        
        
    def getOneSCC(self, vertex, visited, scc):
        scc.append(vertex)
        visited[vertex] = True
        
        for v in self.graph[vertex]:
            if visited[v] == False:
                self.getOneSCC(v, visited, scc)
       
    def computeSCCs(self):
        
        stack = [] # order of stack is the finishing time
        
        ### First DFS: compute the finishing time
        visited = defaultdict(bool) # initialized all notes as unvisited
        
        for i in list(self.graph.keys()): # use outer loop to ganrantee every note will be visited
            if visited[i] == False:
                self.finishingTimeStack(i, visited, stack)
        
        ### Compute a inverse graph
        inverG = self.reverseGraph()
        
        ### Second DFS: compute the SCCs
        SCC_lst = []
        visited =  defaultdict(bool) # initialized all notes as unvisited 
        while stack:
            i = stack.pop()
            if visited[i] == False:
                scc = []
                inverG.getOneSCC(i, visited, scc)
                SCC_lst.append(scc)
        return SCC_lst

## read data
from collections import defaultdict

adj_lst = defaultdict(list)
with open('SCC.txt') as f:
    lines = f.readlines()
    
for line in lines:
    ll = line.strip().split()
    adj_lst[int(ll[0])].append(int(ll[1]))
    
## inverse  
oriG = Graph(adj_lst)
invG = oriG.reverseGraph()


scclist = invG.computeSCCs()

countNote = []
for sublist in scclist:
    countNote.append(len(sublist))
    
with open('sccount.txt', 'w') as f:
    for item in countNote:
        f.write("%s\n" % item)