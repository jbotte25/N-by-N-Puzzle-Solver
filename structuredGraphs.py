#-------------------------------------------
#  structuredGraphs.py
#-------------------------------------------

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack

g = LinkedDirectedGraph()

N=8

# add vertices

for i in range(N**2):
    g.addVertex(i)


# add edges


for i in range(N):
    for j in range(N-1):
        g.addEdge(i*N+j,i*N+j+1,1) #connect horizontial neighbors
        g.addEdge(i*N+j+1,i*N+j,1)
     
       #change out i for j and j for i
for i in range(N):
    for j in range(N-1):
        g.addEdge(j*N+i,j*N+i+N,1) #connect vertical neighbors
        g.addEdge(j*N+i+N,j*N+i,1)
        

print("\n print graph info: ")
print(g)


# ---- Test the DFS traversal ----

def dfs(g, v):
    """ recursive depth-first search """
    v.setMark()
    print(v.getLabel())
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w)


print("\n depth-first search: ")
g.clearVertexMarks()
dfs(g,g.getVertex(0))

# ---- Test the BFS traversal ----

def bfs(g, v):
    """ breadth-first search """
    q=LinkedQueue()
    v.setMark()
    q.add(v)
    while len(q)>0:
        x=q.pop()
        print(x.getLabel())
        for w in g.neighboringVertices(x.getLabel()):
            if not w.isMarked():
                w.setMark()
                q.add(w)
        

print("\n breadth-first search: ")
g.clearVertexMarks()
bfs(g,g.getVertex(0))



