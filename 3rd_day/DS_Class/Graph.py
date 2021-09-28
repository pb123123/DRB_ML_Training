from DS_Class.LinkedList import LinkedList
from DS_Class.Vector import MyVector
import sys

class Graph:
    def __init__(self):
        self.adjlink=LinkedList()

    class GNode:
        def __init__(self, n):
            self.name=n

        def getName(self):
            return self.name

        def setName(self, n):
            self.name=n

    class Edge:
        def __init__(self, o, des, dis):
            self.ori=o
            self.dest=des
            self.dis=dis
        def getOri(self):
            return self.ori

        def getDes(self):
            return self.dest

        def getDistance(self):
            return self.dis

        def printEdge(self):
            print(self.ori.getName(), ",", self.dest.getName(), ",", self.dis, end='')

    def addAdjLink(self, ori, dest, distance):
        #ori=GNode(o)
        #dest=GNode(d)
        edge = self.Edge(ori, dest, distance)
        self.adjlink.insertLast(edge)

    def printGraph(self):
        l=self.adjlink
        cur = l.head
        while cur!=l.trailer:
            if cur!=l.head:
                print("[", end='')
                cur.data.printEdge()
                print("]")
            cur=cur.getNext()

class Dist:
    def __init__(self, D):
        self.dist=D

    def getDist(self, a):
        for i in range(len(self.dist)):
            #print(d[i][0].getName())
            if(self.dist[i][0].getName()==a.getName()):
                return self.dist[i][1]
    def minDistance(self, Q):
        minimum = 10000
        mindistnode = None
        cur = Q.head.getNext()
        while cur!=Q.trailer:
            temp=self.getDist(cur.getElement(), self.dist)
            #print(temp)
            if temp<minimum:
                minimum=temp
                mindistnode=cur
            cur=cur.getNext()
        return mindistnode

    def distOf(u):
        for i in range(len(self.dist)):
            if u==self.dist[i][0]:
                return self.dist[i][1]

    def setDist(u, nd):
        for i in range(len(d)):
            if u==self.dist[i][0]:
                self.dist[i][1]=nd

if __name__ == '__main__':


    def getDist(a, d):
        #print(a.getName())
        for i in range(len(d)):
            #print(d[i][0].getName())
            if(d[i][0].getName()==a.getName()):
                return d[i][1]

    def minDistance(Q, d):
        minimum = 10000
        mindistnode = None
        cur = Q.head.getNext()
        while cur!=Q.trailer:
            temp=getDist(cur.getElement(), d)
            #print(temp)
            if temp<minimum:
                minimum=temp
                mindistnode=cur
            cur=cur.getNext()
        return mindistnode

    def printLL(Q):
        cur = Q.head.getNext()
        print("[", end='')
        while cur != Q.trailer:
            print(cur.data.getName(), ',', end='')
            cur = cur.getNext()
        print(']')

    def neighbors(u, g):
        v=MyVector(100)
        l = g.adjlink
        cur=l.First()
        while cur!=l.Last():
            if(u==cur.getElement().getOri()):
                v.insertLast(cur.getElement())
            cur=cur.getNext()
        return v

    def distOf(u, d):
        for i in range(len(d)):
            if u==d[i][0]:
                return d[i][1]

    def setDist(u, d, nd):
        for i in range(len(d)):
            if u==d[i][0]:
                d[i][1]=nd

    ############################# Initialization
    g=Graph()
    s=g.GNode("s")
    a=g.GNode("a")
    b=g.GNode("b")
    c=g.GNode("c")
    d=g.GNode("d")
    g.addAdjLink(s, a, 10)
    g.addAdjLink(s, c, 5)
    g.addAdjLink(a, c, 2)
    g.addAdjLink(c, a, 3)
    g.addAdjLink(a, b, 1)
    g.addAdjLink(c, b, 9)
    g.addAdjLink(c, d, 2)
    g.addAdjLink(d, s, 7)
    g.addAdjLink(b, d, 4)
    g.addAdjLink(d, b, 6)
    g.printGraph()

    V=LinkedList()
    V.insertLast(s)
    V.insertLast(a)
    V.insertLast(b)
    V.insertLast(c)
    V.insertLast(d)

    #Dist=[[s,0], [a, 1000], [b, 1000], [c, 1000], [d,1000]]
    Dist=[]
    Dist.append([s, 0])
    Dist.append([a, sys.maxsize])
    Dist.append([b, sys.maxsize])
    Dist.append([c, sys.maxsize])
    Dist.append([d, sys.maxsize])

    Q=V
    S=LinkedList()

    #print(distOf(b, Dist))
    #setDist(a, Dist, -100)

    while not Q.isEmpty():
        u=minDistance(Q,Dist)
        #print(u.getElement().getName())
        Q.remove(u)
        #printLL(Q)
        S.insertLast(u)
        #print(u.getName())
        #printLL(S)
        nb = neighbors(u.getElement(), g)
        #print(nb.size)
        #nb.printVector()
        for i in range(nb.size):
            if distOf(nb.elementAt(i).getDes(), Dist) > (distOf(nb.elementAt(i).getOri(), Dist)+nb.elementAt(i).getDistance()):
               setDist(nb.elementAt(i).getDes(), Dist, distOf(nb.elementAt(i).getOri(), Dist)+nb.elementAt(i).getDistance())

    for i in range(len(Dist)):
        print(Dist[i][1])