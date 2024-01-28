from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack
import random

g = LinkedDirectedGraph()

N=5
P=0.25

# add vertices
for i in range(N**2):
    g.addVertex(i)

Blocked=[]
for i in range(1,N**2-1):
    if random.random() < P:
        Blocked.append(i)
print("the blocked nodes are=",Blocked)

# add edges
#connects the neighbors horizontally
for i in range(N):
    for j in range(N-1):
        if i*N+j not in Blocked and i*N+j+1 not in Blocked:
            g.addEdge(i*N+j,i*N+j+1,1)
            g.addEdge(i*N+j+1,i*N+j,1)
        else:
            g.addEdge(i*N+j,i*N+j+1,100)
            g.addEdge(i*N+j+1,i*N+j,100)

# add edges
#connects the neighbors vertically
for i in range(N-1):
    for j in range(N):
        if i*N+j not in Blocked and i*N+j+N not in Blocked:
            g.addEdge(i*N+j,i*N+j+N,1)
            g.addEdge(i*N+j+N,i*N+j,1)
        else:
            g.addEdge(i*N+j,i*N+j+N,100)
            g.addEdge(i*N+j+N,i*N+j,100)

print(g)



