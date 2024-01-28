#-------------------------------------------
#  Examples with Graphs
#-------------------------------------------

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack

g = LinkedDirectedGraph()

# add vertices
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")
g.addVertex("G")

# add edges
g.addEdge("A", "B", 1)
g.addEdge("B", "A", 1)
g.addEdge("A", "C", 1)
g.addEdge("C", "A", 1)
g.addEdge("B", "D", 1)
g.addEdge("D", "B", 1)
g.addEdge("E", "C", 1)
g.addEdge("C", "E", 1)
g.addEdge("E", "G", 1)
g.addEdge("G", "E", 1)
g.addEdge("E", "D", 1)
g.addEdge("D", "E", 1)
g.addEdge("E", "B", 1)
g.addEdge("B", "E", 1)
g.addEdge("G", "D", 1)
g.addEdge("D", "G", 1)
g.addEdge("G", "F", 1)
g.addEdge("F", "G", 1)
g.addEdge("F", "B", 1)
g.addEdge("B", "F", 1)




# Try out some methods

print("\n print graph info: ")
print(g)


print("\n neighboring vertices of A:")
for vertex in g.neighboringVertices("A"):
    print(vertex)


print("\n incident edges of A:")
for edge in g.incidentEdges("A"):
    print(edge)

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
dfs(g,g.getVertex("A"))

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
bfs(g,g.getVertex("A"))



'''
from linkedbst import *

myTree=LinkedBST()

myTree.add(50)
myTree.add(33)
myTree.add(45)
myTree.add(67)
myTree.add(53)
myTree.add(89)
myTree.add(65)
myTree.add(70)
myTree.add(21)
myTree.add(43)
myTree.add(76)
myTree.add(30)
myTree.add(49)
myTree.add(51)

myTree.remove(67)
myTree.remove(50)


print(myTree)
print('InOrder:',myTree.postorder())
print('Sum of values:',myTree.sum())
print('Number of nodes:',myTree.count())
print('Height of tree:',myTree.height())
print('Is the tree full:',myTree.isFull())

print('--------------------------------------------------\n')
print('--------------------------------------------------\n')

tree2=LinkedBST()
tree2.add(25)
tree2.add(12)
tree2.add(30)
tree2.add(8)
tree2.add(27)
tree2.add(32)
tree2.add(26)
tree2.add(7)
tree2.add(13)
tree2.add(5)
tree2.add(3)

print(tree2)
print('Sum of values:',tree2.sum())
print('Number of nodes:',tree2.count())
print('Height of tree:',tree2.height())
print('Is the tree full:',tree2.isFull())

print('--------------------------------------------------\n')
print('--------------------------------------------------\n')

tree3=LinkedBST()
tree3.add(22)
tree3.add(11)
tree3.add(34)
tree3.add(9)
tree3.add(20)
tree3.add(24)
tree3.add(45)


print(tree3)
print('Sum of values:',tree3.sum())
print('Number of nodes:',tree3.count())
print('Height of tree:',tree3.height())
print('Is the tree full:',tree3.isFull())
'''
