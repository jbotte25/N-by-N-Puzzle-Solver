#-------------------------------------------
#  Prim's Algorithm Implementation
#-------------------------------------------

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack
import random

def prim(g, i):
    '''
    Prim's Algorithm
    returns the minimal spanning tree (mst)
    for graph g, starting with vertex i
    '''

    # initialize values
    n=g.sizeVertices()  # number of vertices to add
    D=[]    # D[i] is the cost/distance to add vertex i
    V=[]    # V[i] is the vertex in the MST adjacent to i 
    for j in range(0,n):
        D.append(float('inf'))
        V.append(None)

    # create MST and add vertex i into it 
    D[i]=0  
    mst = LinkedDirectedGraph()
    mst.addVertex(i)
    g.getVertex(i).setMark()

    # recently added vertex
    minIndex=i

    # add vertices until the mst has as many vertices as g
    while mst.sizeVertices()<n:

        # update D and V based on minIndex 
        for w in g.neighboringVertices(minIndex):
                if not w.isMarked():
                    k=w.getLabel()
                    edgeVal = g.getEdge(minIndex,k).getWeight()
                    if D[k]>edgeVal:
                        D[k]=edgeVal
                    #if D[k]>D[minIndex]+edgeVal: #taking the minIndex from the previous node and adding the edgeVal to that
                        #D[k]=edgeVal+D[minIndex]
                        V[k]=minIndex

      
        # find the first unvisited vertex
        k=-1
        j=0
        while k<0 and j<n:
            if not g.getVertex(j).isMarked():
                k=j
            j+=1

        # find minimum cost unvisited vertex
        minIndex=k
        for j in range(0,n):    
            if not g.getVertex(j).isMarked():
                if D[j]<D[minIndex]:
                    minIndex=j

        # add new vertex to the MST and mark it in g
        edgeVal = g.getEdge(V[minIndex],minIndex).getWeight()
        mst.addVertex(minIndex)
        mst.addEdge(minIndex,V[minIndex],edgeVal)
        mst.addEdge(V[minIndex],minIndex,edgeVal)

        g.getVertex(minIndex).setMark()
    print(D)
    print(V)

    return mst

#-----------------------------------
# Test out the method below
'''
g = LinkedDirectedGraph()

N=int(input("Enter a number please:")) #Number of nodes
P=.2 #Percentage of nodes being blocked out

# add vertices

for i in range(N**2):
    g.addVertex(i)

# add edges
#connects the horizontal neighbors
for i in range(N):
    for j in range(N-1):
            g.addEdge(i*N+j,i*N+j+1,1) 
            g.addEdge(i*N+j+1,i*N+j,1)
        
#connects the vertical neighbors
for i in range(N):
    for j in range(N-1):
            g.addEdge(j*N+i,j*N+i+N,1) 
            g.addEdge(j*N+i+N,j*N+i,1)
'''
for i in range(1,N**2-1):
    if random.random()<P:
        g.removeVertex(i)
        g.addVertex(i)
'''        

#blocks out nodes

Blocked=[]
for i in range(1,N**2-1):
    if random.random() < P:
        g.removeVertex(i)
        Blocked.append(i)
    
        
print('N =',N)
print('P = ',P)
print('Blocked nodes=',Blocked) 
print(g)
m=prim(g,0)
'''
g = LinkedDirectedGraph()

# add vertices
for i in range(0,6):
    g.addVertex(i)

# add edges
g.addEdge(0,1,24)
g.addEdge(1,0,24)
g.addEdge(0,3,15)
g.addEdge(3,0,15)
g.addEdge(0,5,22)
g.addEdge(5,0,22)
g.addEdge(1,2,18)
g.addEdge(2,1,18)
g.addEdge(1,3,13)
g.addEdge(3,1,13)
g.addEdge(1,5,10)
g.addEdge(5,1,10)
g.addEdge(2,4,17)
g.addEdge(4,2,17)
g.addEdge(3,4,11)
g.addEdge(4,3,11)

# Try out some methods

print("\n print graph info : g ")
print(g)

m=prim(g,2)

print("\n print graph info : mst ")
print(m)

