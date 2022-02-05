from copy import deepcopy
"""
BFS Application:
    * Shortest Path and Minimum Spanning Tree for unweighted graph # but use Dikastra or Bellman-Ford
    * All Possible Path # but use Dikastra or Bellman-Ford
"""

"""
DFS Application:
    * Detecting cycle in a graph
    * Path Finding
    * Topological Sorting
"""
class LinkedListNode():
    def __init__(self, neighbour=None, next=None):
        self.neighbour=neighbour
        self.next=next

class GraphNode():
    def __init__(self, vertex=None, neighbour=None, next=None):
        self.vertex=vertex
        self.neighbours=LinkedListNode(neighbour=neighbour)
        self.next=next

class BFSApplication():
    def __init__(self):
        self.node=GraphNode()

    def insert(self, vertex, neighbour):
        if self.node is None or self.node.vertex is None:
            self.node=GraphNode(vertex=vertex, neighbour=neighbour)
        else:
            ptr=self.node
            while True:
                if ptr is not None and ptr.vertex is not None:
                    if ptr.vertex==vertex:
                        nptr=ptr.neighbours
                        while True:
                            if nptr is not None and nptr.neighbour is not None:
                                if nptr.neighbour==neighbour:
                                    break
                                elif nptr.next is not None:
                                    nptr=nptr.next
                                elif nptr.next is None:
                                    nptr.next=LinkedListNode(neighbour=neighbour)
                                    break
                        break
                    elif ptr.next is not None:
                        ptr=ptr.next
                    elif ptr.next is None:
                        ptr.next=GraphNode(vertex=vertex, neighbour=neighbour)
                        break

    def display(self):
        ptr=self.node
        while True:
            if ptr is not None and ptr.vertex is not None:
                print("Vertex:", ptr.vertex, "-> ", end="")
                nptr=ptr.neighbours
                neighbours=[]
                while True:
                    if nptr is not None and nptr.neighbour is not None:
                        neighbours.append(nptr.neighbour)
                        nptr=nptr.next
                    else:
                        break
                print("Neighbours:", neighbours)
                ptr=ptr.next
            else:
                break

    def findminpath(self, start, end, path=None, queue=[], visited=[], init=True):
        if init:
            queue=[start,]
            visited=[start,]
            init=False
        ptr=self.node
        nptr=None
        while True:
            if ptr is not None and ptr.vertex is not None:
                if ptr.vertex==start:
                    nptr=ptr.neighbours
                    break
                ptr=ptr.next
            else:
                break
        while True:
            if nptr is not None and nptr.neighbour is not None:
                if nptr.neighbour not in visited:
                    if nptr.neighbour==end:
                        if path is None:
                            path=queue+[nptr.neighbour]
                        else:
                            if len(path)>len(queue+[nptr.neighbour]):
                                path=queue+[nptr.neighbour]
                        break
                    path=self.findminpath(nptr.neighbour, end, path, queue+[nptr.neighbour], visited+[nptr.neighbour], init)
                nptr=nptr.next
            else:
                break
        return path

    def findallpath(self, start, end, queue, visited):
        ptr=self.node
        nptr=None
        while True:
            if ptr is not None and ptr.vertex is not None:
                if ptr.vertex==start:
                    nptr=ptr.neighbours
                    break
                else:
                    ptr=ptr.next
            else:
                break
        while True:
            if nptr is not None and nptr.neighbour is not None:
                if nptr.neighbour not in visited:
                    if nptr.neighbour==end:
                        print(queue+[end])
                    else:
                        start=nptr.neighbour
                        self.findallpath(start, end, queue+[start], visited+[start])
                nptr=nptr.next
            else:
                break
        return

class DFSApplication():
    def __init__(self):
        self.node=GraphNode()

    def insert(self, vertex, neighbour):
        if self.node is None or self.node.vertex is None:
            self.node=GraphNode(vertex=vertex, neighbour=neighbour)
        else:
            ptr=self.node
            while True:
                if ptr.vertex==vertex:
                    nptr=ptr.neighbours
                    while True:
                        if nptr.neighbour==neighbour:
                            break
                        else:
                            if nptr.next is None or nptr.next.neighbour is None:
                                nptr.next=LinkedListNode(neighbour=neighbour)
                                break
                            else:
                                nptr=nptr.next
                    break
                else:
                    if ptr.next is None or ptr.next.vertex is None:
                        ptr.next=GraphNode(vertex=vertex, neighbour=neighbour)
                        break
                    else:
                        ptr=ptr.next

    def display(self):
        ptr=self.node
        while True:
            if ptr is not None and ptr.vertex is not None:
                print("Vertex:", ptr.vertex, "-> ", end="")
                nptr=ptr.neighbours
                neighbours=[]
                while True:
                    if nptr is not None and nptr.neighbour is not None:
                        neighbours.append(nptr.neighbour)
                        nptr=nptr.next
                    else:
                        break
                print("Neighbours:", neighbours)
                ptr=ptr.next
            else:
                break

    def topologicalsortingutil(self, ptr, stack, visited):
        if ptr!=None and ptr.vertex!=None:
            visited.append(ptr.vertex)
            nptr=ptr.neighbours
            while nptr!=None and nptr.neighbour!=None:
                if nptr.neighbour not in visited:
                    ptr_dash=self.node
                    check=True
                    while ptr_dash!=None and ptr_dash.vertex!=None:
                        if ptr_dash.vertex==nptr.neighbour:
                            stack, visited=self.topologicalsortingutil(ptr_dash, stack, visited)
                            check=False
                        ptr_dash=ptr_dash.next
                    if check:
                        visited.append(nptr.neighbour)
                        stack.append(nptr.neighbour)
                nptr=nptr.next
            stack.append(ptr.vertex)

        return stack, visited


    def topologicalsorting(self, visited=[], stack=[]):
        ptr=self.node
        while ptr!=None and ptr.vertex!=None:
            if ptr.vertex not in visited:
                stack, visited=self.topologicalsortingutil(ptr, stack, visited)
            ptr=ptr.next
        print("Topological Sorting: ", end="")
        while len(stack)>0:
            print(stack.pop(), "-> ",end="")
        print("End")

    def findpath(self, start, end):
        visited=[start,]
        stack=[start,]
        vertex=stack[-1]
        while vertex is not None:
            ptr=self.node
            nptr=None
            while True:
                if ptr is not None and ptr.vertex is not None:
                    if ptr.vertex==vertex:
                        nptr=ptr.neighbours
                        break
                    else:
                        ptr=ptr.next
                else:
                    break
            while True:
                if nptr is not None and nptr.neighbour is not None:
                    if nptr.neighbour not in visited:
                        visited.append(nptr.neighbour)
                        stack.append(nptr.neighbour)
                        #if nptr.neighbour==end and stack[0]==start:
                        if nptr.neighbour==end:
                            print(stack)
                            stack=[]
                        break
                    else:
                        nptr=nptr.next
                else:
                    if len(stack)>0:
                        stack.pop()
                        """
                        if len(stack)==0:
                            ptr=self.node
                            while True:
                                if ptr is not None and ptr.vertex is not None:
                                    if ptr.vertex not in visited:
                                        visited.append(ptr.vertex)
                                        stack.append(ptr.vertex)
                                        break
                                    else:
                                        ptr=ptr.next
                                else:
                                    break
                        """
                    break
            vertex=stack[-1] if len(stack)>0 else None

    def detectcycle(self):
        stack=[self.node.vertex,]
        visited=[self.node.vertex,]
        vertex=stack[-1]
        while vertex is not None:
            ptr=self.node
            nptr=None
            while True:
                if ptr is not None and ptr.vertex is not None:
                    if ptr.vertex==vertex:
                        nptr=ptr.neighbours
                        break
                    else:
                        ptr=ptr.next
                else:
                    break
            while True:
                if nptr is not None and nptr.neighbour is not None:
                    i=0
                    init=False
                    while i<len(stack):
                        if nptr.neighbour==stack[i] or init:
                            print(stack[i], "-> ", end="")
                            init=True
                        i+=1
                        if i==len(stack) and init:
                            print(nptr.neighbour)
                            init=False
                    if nptr.neighbour not in visited:
                        stack.append(nptr.neighbour)
                        visited.append(nptr.neighbour)
                        break
                    else:
                        nptr=nptr.next
                else:
                    if len(stack)>0:
                        stack.pop()
                        if len(stack)==0:
                            ptr=self.node
                            while True:
                                if ptr is not None and ptr.vertex is not None:
                                    if ptr.vertex not in visited:
                                        stack.append(ptr.vertex)
                                        visited.append(ptr.vertex)
                                        break
                                    else:
                                        ptr=ptr.next
                                else:
                                    break
                    break
            vertex=stack[-1] if len(stack)>0 else None


def main():
    mode=input("Mode: ").lower()
    if mode=="bfs":
        bfsapplication=BFSApplication()
        while True:
            choice=int(input("Graph\n1: Insert\n2: Find Min Path\n3: Find All Paths\n0: Exit\nChoice: "))
            if choice==0:
                break
            elif choice==1:
                vertex=input("Vertex: ").strip()
                neighbours=list(map(str, input("Neighbours: ").split()))
                for neighbour in neighbours:
                    bfsapplication.insert(vertex, neighbour)
                bfsapplication.display()
            elif choice==2:
                start=input('Start: ').strip()
                end=input('End: ').strip()
                print(bfsapplication.findminpath(start, end))
            elif choice==3:
                start=input('Start: ').strip()
                end=input('End: ').strip()
                queue=[start,]
                visited=[start,]
                bfsapplication.findallpath(start, end, queue, visited)

    elif mode=="dfs":
        dfsapplication=DFSApplication()
        while True:
            choice=int(input("Graph\n1: Insert\n2: Sorting\n3: Find Path\n4: Detect Cycle\n0: Exit\nChoice: "))
            if choice==0:
                break
            elif choice==1:
                vertex=input("Vertex: ").strip()
                neighbours=list(map(str, input("Neighbours: ").split()))
                for neighbour in neighbours:
                    dfsapplication.insert(vertex, neighbour)
                dfsapplication.display()
            elif choice==2:
                dfsapplication.topologicalsorting()
            elif choice==3:
                dfsapplication.findpath(input('Start: ').strip(), input('End: ').strip())
            elif choice==4:
                dfsapplication.detectcycle()
    else:
        print("Invalid Mode!!")


if __name__ == '__main__':
    main()
