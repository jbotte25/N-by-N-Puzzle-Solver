#-----------------------------------------------
#  Dijkstra's Algorithm Implementation
#-----------------------------------------------

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack
import random

def dijkstra(g, i):
   
    # initialize values
    n=g.sizeVertices()  # number of vertices to add
    D=[]    # D[i] is the cost/distance to add vertex i
    V=[]    # V[i] is the vertex in the MST adjacent to i
    for j in range(0,n):
        D.append(float('inf'))
        V.append(None)

    # create MST and add vertex i into it
    #Dont need in Dijkstra's
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
                if D[k]>D[minIndex]+edgeVal: #taking the minIndex from the previous node and adding the edgeVal to that
                    D[k]=edgeVal+D[minIndex] #edgeVal + minIndex from the prevoius node
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
        #edgeVal = g.getEdge(V[minIndex],minIndex).getWeight()
        mst.addVertex(minIndex)
        #mst.addEdge(minIndex,V[minIndex],edgeVal)
        #mst.addEdge(V[minIndex],minIndex,edgeVal)

        g.getVertex(minIndex).setMark()
   
    print('D =',D)
    print('V =',V)
    if D[-1]>100:
        print("The graph cannot be completed")
    else:
        path=[]
        i=N**2-1
        while V[i] != None:
            path.append(i)
            k=V[i]
            i=k
        path.append(0)
        path.reverse()
        print('The fastest way  to get from 0-N is:',path)
    

#-----------------------------------
# Test out the method below
g = LinkedDirectedGraph()

N=int(input("Enter a number please:"))
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
            
print('N =',N)
print('P =',P)
#print(g)
dijkstra(g,0)
