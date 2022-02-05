"""
0 - 1 3
1 - 0 2 3 5 6
2 - 1 3 4 5
3 - 0 1 2 4
4 - 2 3 6
5 - 1 2
6 - 1 4
"""

class LinkedListNode():
    def __init__(self, info=None, next=None):
        self.info=info
        self.next=next

class Node():
    def __init__(self, vertice=None, neighbour=None, next=None):
        self.vertice=vertice
        self.neighbours=LinkedListNode(info=neighbour)
        self.next=next

class Graph():
    def __init__(self):
        self.node=Node()

    def insert(self, vertice, neighbour):
        if self.node==None or self.node.vertice==None:
            self.node=Node(vertice=vertice, neighbour=neighbour)
        else:
            verticeExists=False
            ptr=self.node
            while True:
                if ptr.vertice!=vertice:
                    if ptr.next!=None and ptr.next.vertice!=None:
                        ptr=ptr.next
                    else:
                        break
                else:
                    verticeExists=True
                    neighbourExists=False
                    nptr=ptr.neighbours
                    while nptr.next!=None and nptr.next.info!=None:
                        if nptr.info!=neighbour:
                            nptr=nptr.next
                        else:
                            neighbourExists=True
                            break
                    if not neighbourExists:
                        nptr.next=LinkedListNode(info=neighbour)
                    break
            if not verticeExists:
                ptr.next=Node(vertice=vertice, neighbour=neighbour)

    def display(self):
        ptr=self.node
        print("Graph: ")
        while ptr!=None and ptr.vertice!=None:
            print("Vertice:", ptr.vertice, "-> neighbour:", end="")
            nptr=ptr.neighbours
            while nptr!=None and nptr.info!=None:
                print(nptr.info, "-> ", end="")
                nptr=nptr.next
            print("End")
            ptr=ptr.next

class DFS():
    def __init__(self, node):
        self.node=node
        self.stack=[]
        self.visited=[]

    def traversal(self):
        ptr=self.node
        self.stack.append(ptr.vertice)
        self.visited.append(ptr.vertice)
        if ptr!=None and ptr.vertice!=None:
            print(self.node.vertice, "-> ", end="")
        while True:
            if ptr!=None and ptr.vertice!=None:
                neighbours=ptr.neighbours
                while True:
                    if neighbours.info not in self.visited:
                        print(neighbours.info, "-> ", end="")
                        self.stack.append(neighbours.info)
                        self.visited.append(neighbours.info)
                        break
                    else:
                        neighbours=neighbours.next
                        if neighbours==None or neighbours.info==None:
                            self.stack.pop()
                            break
                ptr=self.node
                while len(self.stack)>0 and self.stack[-1]!=ptr.vertice:
                    ptr=ptr.next
                    if ptr==None or ptr.vertice==None:
                        self.stack.pop()
                        ptr=self.node
                if len(self.stack)==0:
                    break
        print("End")

class BFS():
    def __init__(self, node):
        self.node=node
        self.queue=[]
        self.visited=[]

    def traversal(self):
        ptr=self.node
        self.queue.append(ptr.vertice)
        self.visited.append(ptr.vertice)
        while ptr!=None and ptr.vertice!=None:
            nptr=ptr.neighbours
            while nptr!=None and nptr.info!=None:
                if nptr.info not in self.visited:
                    self.queue.append(nptr.info)
                    self.visited.append(nptr.info)
                nptr=nptr.next
            print(self.queue.pop(0), "-> ", end="")
            ptr=self.node
            while len(self.queue)>0 and self.queue[0]!=ptr.vertice:
                ptr=ptr.next
                if ptr==None or ptr.vertice==None:
                    print(self.queue.pop(0), "-> ", end="")
                    ptr=self.node
            if len(self.queue)==0:
                break
        print("End")

def main():
    graph=Graph()
    process=True
    while process:
        print('1:Insert\n2:BFS\n3:DFS\n4:Exit')
        try:
            choice=input('Enter Choice:')
            if choice=='4':
                process=False
                break
            elif choice=='1':
                vertice=int(input('Vertice:'))
                neighbours=list(map(int, input('Neighbours:').split()))
                for neighbour in neighbours:
                    graph.insert(vertice=vertice, neighbour=neighbour)
                graph.display()
            elif choice=='2':
                bfs=BFS(node=graph.node)
                bfs.traversal()
            elif choice=='3':
                dfs=DFS(node=graph.node)
                dfs.traversal()
            else:
                print('Alert: Enter Valid Input!')
        except ValueError:
            print('Alert: Enter Valid Input!')

if __name__ == '__main__':
    main()
