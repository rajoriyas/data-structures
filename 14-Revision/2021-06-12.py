import math
class Node():
    def __init__(self, info=None, next=None):
        self.info = info
        self.next = next

class LinkedList():
    def __init__(self):
        self.node = Node()
        self.ptr = Node()
        self.len = 0

    def insert(self, info, pos=1, verbose=True):
        if self.len == 0:
            self.node = Node(info=info)
        elif self.len > 0:
            if pos == 1:
                self.node = Node(info=info, next=self.node)
            elif pos in range(2, self.len+1):
                i = 1
                self.ptr = self.node
                while i < pos-1:
                    self.ptr = self.ptr.next
                    i += 1
                self.ptr.next = Node(info=info, next=self.ptr.next)
            elif pos == self.len+1:
                i = 1
                self.ptr = self.node
                while i < pos-1:
                    self.ptr = self.ptr.next
                    i += 1
                self.ptr.next = Node(info=info)
        self.len += 1
        if verbose:
            self.show()

    def delete(self, pos=1, verbose=True):
        if self.len > 0:
            if pos == 1:
                self.node = self.node.next
            elif pos in range(1, self.len):
                i = 1
                self.ptr = self.node
                while i < pos-1:
                    self.ptr = self.ptr.next
                    i += 1
                self.ptr.next = self.ptr.next.next
            elif pos == self.len:
                i = 1
                self.ptr = self.node
                while i < pos-1:
                    self.ptr = self.ptr.next
                    i += 1
                self.ptr.next = Node()
            self.len -= 1
        if verbose:
            self.show()

    def show(self):
        i = 1
        self.ptr = self.node
        print("Linked List: ", sep="", end="")
        while i <= self.len:
            print(str(self.ptr.info)+"->", sep="", end="")
            self.ptr = self.ptr.next
            i += 1
        print('END Length: '+str(self.len))

class CircularQueue():
    def __init__(self, size):
        self.cqueue = [None]*size
        self.front = -1
        self.rear = -1
        self.size = size

    def enqueue(self, val):
        if self.front == self.rear%self.size:
            print('Overflow')
        else:
            if self.rear == -1 and self.front == -1:
                self.rear += 1
                self.front += 1
            self.cqueue[self.rear] = val
            self.rear = (self.rear+1)%self.size
        print('Circular Queue:'+ str(self.cqueue), self.rear, self.front)

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print('Underflow')
        else:
            self.cqueue[self.front] = None
            self.front = (self.front+1)%self.size
            if self.front == self.rear%self.size:
                self.front = -1
                self.rear = -1
        print('Circular Queue:'+ str(self.cqueue), self.rear, self.front)

class Sorting():
    def __init__(self, list):
        self.list = list

    """
    MERGE SORT
    """
    def expand(self, list):
        if len(list)>1:
            mid = len(list)//2
            list = self.shrink(self.expand(list[:mid]), self.expand(list[mid:]))
        return list

    def shrink(self, pre, post):
        list = []
        i=j=0
        while i<len(pre) and j<len(post):
            if pre[i]<post[j]:
                list.append(pre[i])
                i += 1
            else:
                list.append(post[j])
                j += 1
        while i < len(pre):
            list.append(pre[i])
            i += 1
        while j < len(post):
            list.append(post[j])
            j += 1
        return list

    def merge(self):
        list = self.list
        return self.expand(list)

    """
    SHELL SORT
    """
    def shell(self, list, step=1):
        i, interval = 0, (len(list)-1)//(2**step)
        while i+interval<len(list):
            if list[i+interval]<list[i]:
                list[i+interval], list[i] = list[i], list[i+interval]
                j=i
                while j-interval>=0:
                    if list[j]<list[j-interval]:
                        list[j-interval], list[j] = list[j], list[j-interval]
                        j-=interval
                    else:
                        j=interval-1
            i+=1
        if interval>1:
            list = self.shell(list, step+1)
        return list

    def partition(self, list, pivot, start):
        i, j = start, start-1
        while i<pivot:
            if list[pivot]>=list[i]:
                j+=1
                list[j], list[i] = list[i], list[j]
            i+=1
        j+=1
        list[j], list[pivot] = list[pivot], list[j]
        return list, j

    def quick(self, list, pivot, start=0):
        """
        END PIVOT
        """
        end = pivot
        if end>start:
            list, pivot = self.partition(list=list, pivot=pivot, start=start)
            list = self.quick(list=list, pivot=pivot-1, start=start)
            list = self.quick(list, pivot=end, start=pivot+1)
        return list

class Searching():
    def __init__(self, list):
        self.sort = Sorting(list)
        self.list = self.sort.quick(list=self.sort.list, pivot=len(self.sort.list)-1)

    def interpolation(self, val, lb, ub):
        index = -1
        if lb<ub:
            pos = lb + ( ( (ub-lb) // (self.list[ub]-self.list[lb]) ) * (val-self.list[lb]) )
            if self.list[pos] == val:
                index = self.list.index(val)
            elif self.list[pos] < val:
                index = self.interpolation(val=val, lb=pos+1, ub=ub)
            else:
                index = self.interpolation(val=val, lb=lb, ub=pos-1)
        return index

class HeapNode():
    def __init__(self, info=None, left=None, right=None):
        self.info=info
        self.left=left
        self.right=right

class Heap():
    def __init__(self):
        """
        https://www.geeksforgeeks.org/binary-heap/
        """
        self.node=HeapNode()

    def insert(self, info):
        info=int(info)
        if self.node is None or self.node.info is None:
            self.node=HeapNode(info=info)
        else:
            queue=[self.node,]
            i=0
            inserted = False
            while i<len(queue):
                ptr=queue[i]
                if ptr.left is None or ptr.left.info is None:
                    ptr.left=HeapNode(info=info)
                    inserted = True
                elif ptr.right is None or ptr.right.info is None:
                    ptr.right=HeapNode(info=info)
                    inserted = True
                i+=1
                if ptr.left is not None and ptr.left.info is not None:
                    queue.append(ptr.left)
                if ptr.right is not None and ptr.right.info is not None:
                    queue.append(ptr.right)
                if inserted:
                    break
            self.heapify(queue)
        self.show(self.node)
        print()

    def delete(self):
        if self.node is not None or self.node.info is not None:
            queue=[self.node,]
            i=0
            while i<len(queue):
                ptr=queue[i]
                if ptr.left is not None and ptr.left.info is not None:
                    queue.append(ptr.left)
                if ptr.right is not None and ptr.right.info is not None:
                    queue.append(ptr.right)
                i+=1
            """
            Due to this, (queue[i-1].info = None), we've to check that ptr/node.info is None or not with ptr/node is None every where.
            """
            queue[0].info, queue[i-1].info = queue[i-1].info, None
            queue.pop()
            self.heapify(queue)
        self.show(self.node)
        print()

    def show(self, node, mode='(N)'):
        if node.left is not None and node.left.info is not None:
            self.show(node.left, mode='(L)')
        print(node.info, mode, end=" -> ")
        if node.right is not None and node.right.info is not None:
            self.show(node.right, mode='(R)')

    def heapify(self, queue):
        """
        MAX HEAP

        Arr[(i-1)/2]	Returns the parent node
        Arr[(2*i)+1]	Returns the left child node
        Arr[(2*i)+2]	Returns the right child node
        """
        i=0
        while len(queue)>0 and i<len(queue):
            if ((2*i)+1)<len(queue) and queue[(2*i)+1].info>queue[i].info:
                queue[(2*i)+1].info, queue[i].info = queue[i].info, queue[(2*i)+1].info
                j=i
                while j>=0:
                    if (j-1)//2>=0 and queue[j].info>queue[(j-1)//2].info:
                        queue[(j-1)//2].info, queue[j].info = queue[j].info, queue[(j-1)//2].info
                        j=(j-1)//2
                    else:
                        j=-1
            if ((2*i)+2)<len(queue) and queue[(2*i)+2].info>queue[i].info:
                queue[(2*i)+2].info, queue[i].info = queue[i].info, queue[(2*i)+2].info
                j=i
                while j>=0:
                    if (j-1)//2>=0 and queue[j].info>queue[(j-1)//2].info:
                        queue[(j-1)//2].info, queue[j].info = queue[j].info, queue[(j-1)//2].info
                        j=(j-1)//2
                    else:
                        j=-1
            i+=1

class AVLNode():
    def __init__(self, info=None, left=None, right=None, bf=0):
        self.info=info
        self.left=left
        self.right=right
        self.bf=bf

class AVLTree():
    def __init__(self):
        self.node=AVLNode()

    def insert(self, info):
        if self.node is None or self.node.info is None:
            self.node=AVLNode(info=info)
        else:
            ptr=self.node
            while ptr is not None and ptr.info is not None:
                if ptr.info>info:
                    if ptr.left is None or ptr.left.info is None:
                        ptr.left=AVLNode(info=info)
                    else:
                        ptr=ptr.left
                elif ptr.info<info:
                    if ptr.right is None or ptr.right.info is None:
                        ptr.right=AVLNode(info=info)
                    else:
                        ptr=ptr.right
                else:
                    break
            self.calculateBF(self.node)
            self.rotate()
        self.show(self.node)
        print()

    def delete(self, info):
        if self.node is not None or self.node.info is not None:
            ptr=self.node
            while ptr is not None and ptr.info is not None:
                if ptr.info==info:
                    if (ptr.left is None or ptr.left.info is None) and (ptr.right is None or ptr.right.info is not None):
                        ptr.info = None
                    elif (ptr.left is not None and ptr.left.info is not None) and (ptr.right is None or ptr.right.info is None):
                        ptr.info, ptr.left, ptr.right = ptr.left.info, ptr.left.left, ptr.left.right
                    elif (ptr.right is not None and ptr.right.info is not None) and (ptr.left is None or ptr.left.info is None):
                        ptr.info, ptr.left, ptr.right = ptr.right.info, ptr.right.left, ptr.right.right
                    else:
                        """
                        METHOD:
                            Inorder Predecessor
                            Inorder Successor (USED)
                        """
                        if ptr.right.left is None or ptr.right.left.info is None:
                            ptr.info, ptr.right=ptr.right.info, ptr.right.right
                        else:
                            print(ptr.info)
                            temp=ptr.right
                            while temp.left is not None:
                                temp = temp.left
                            print(temp.info)
                            if temp.right is not None and temp.right.info is not None:
                                ptr.info, temp.info, temp.right = temp.info, temp.right.info, temp.right.right
                            else:
                                ptr.info, temp.info = temp.info, None
                    break
                elif ptr.info>info:
                    ptr=ptr.left
                elif ptr.info<info:
                    ptr=ptr.right
            self.calculateBF(self.node)
            self.rotate()
        self.show(self.node)
        print()

    def calculateBF(self, node):
        left=right=1
        if node.left is not None and node.left.info is not None:
            left+=self.calculateBF(node.left)
        if node.right is not None and node.right.info is not None:
            right+=self.calculateBF(node.right)
        node.bf=right-left
        return max(right, left)

    def mode(self, node, mode=""):
        if node is not None:
            left=right=""
            if node.left is not None and node.left.info is not None:
                left=self.mode(node.left, mode=mode+'L')
            if node.right is not None and node.right.info is not None:
                right=self.mode(node.right, mode=mode+'R')
            if len(left)>len(right):
                mode=left
            elif len(left)<len(right):
                mode=right
        return mode

    def rotate(self):
        while abs(self.node.bf)>1:
            mode = self.mode(self.node)[:2]
            print('Mode:', mode)
            if mode == 'LL':
                self.node.info, self.node.left, self.node.right = self.node.left.info, self.node.left.left, AVLNode(info=self.node.info, left=self.node.left.right, right=self.node.right)
            elif mode == 'RR':
                self.node.info, self.node.left, self.node.right = self.node.right.info, AVLNode(info=self.node.info, left=self.node.left, right=self.node.right.left), self.node.right.right
            elif mode == 'RL':
                self.node.info, self.node.left, self.node.right.left = self.node.right.left.info, AVLNode(info=self.node.info, left=self.node.left, right=self.node.right.left.left), self.node.right.left.right
            elif mode == 'LR':
                self.node.info, self.node.right, self.node.left.right = self.node.left.right.info, AVLNode(info=self.node.info, left=self.node.left.right.right, right=self.node.right), self.node.left.right.left
            self.calculateBF(self.node)

    def show(self, node, mode="(N)"):
        if node is not None and node.info is not None:
            print(node.info, "(BF: "+str(node.bf)+")", mode, end=" -> ")
        if node.left is not None and node.left.info is not None:
            self.show(node.left, mode="(L)")
        if node.right is not None and node.right.info is not None:
            self.show(node.right, mode="(R)")

class GraphNode():
    def __init__(self, prev=None, vertice=None, neighbour=None, next=None):
        self.prev=prev
        self.vertice=vertice
        self.neighbour=LinkedList()
        self.neighbour.insert(info=neighbour, pos=self.neighbour.len+1, verbose=False)
        self.next=next

class Graph():
    def __init__(self):
        self.node=GraphNode()

    def insert(self, vertice, neighbour):
        if self.node is None or self.node.vertice is None:
            self.node=GraphNode(vertice=vertice, neighbour=neighbour)
        else:
            inserted = False
            prev=ptr=self.node
            while ptr is not None and ptr.vertice is not None:
                if ptr.vertice==vertice:
                    ptr.neighbour.insert(info=neighbour, pos=ptr.neighbour.len+1, verbose=False)
                    inserted=True
                    break
                else:
                    prev, ptr = ptr, ptr.next
            if not inserted:
                prev.next=GraphNode(vertice=vertice, neighbour=neighbour)

    def show(self):
        ptr=self.node
        while ptr is not None and ptr.vertice is not None:
            print("Vertice:", ptr.vertice, end="-")
            ptr.neighbour.show()
            ptr=ptr.next

    def bfs(self, queue=[], rear=0, front=0):
        if self.node is not None and self.node.vertice is not None:
            queue.insert(rear, self.node.vertice)
            rear+=1
            while rear!=-1 and front!=-1:
                # Searching start
                found = False
                ptr = self.node
                while ptr is not None and ptr.vertice is not None:
                    if ptr.vertice==queue[front]:
                        found = True
                        break
                    ptr=ptr.next
                # Searching enf
                # Insertion start
                if found:
                    neighbour = ptr.neighbour.node
                    while neighbour is not None and neighbour.info is not None:
                        if neighbour.info not in queue:
                            queue.insert(rear, neighbour.info)
                            rear+=1
                        neighbour=neighbour.next
                # Insertion end
                # Display start
                print(queue[front], end="->")
                front+=1
                #Display end
                if front==rear:
                    print('END', len(queue))
                    rear=-1
                    front=-1

    def dfs(self, stack=[], top=-1, out=[]):
        if self.node is not None and self.node.vertice is not None:
            stack.append(self.node.vertice)
            top+=1
            while len(stack)>0:
                if stack[top] not in out:
                    out.append(stack[top])
                    print(stack[top], end="->")
                found = False
                ptr = self.node
                while ptr is not None and ptr.vertice is not None:
                    if ptr.vertice==stack[top]:
                        found = True
                        break
                    ptr=ptr.next
                inserted = False
                if found:
                    neighbour = ptr.neighbour.node
                    while neighbour is not None and neighbour.info is not None:
                        if neighbour.info not in stack and neighbour.info not in out:
                            stack.append(neighbour.info)
                            top+=1
                            inserted=True
                            break
                        neighbour=neighbour.next
                if not inserted:
                    stack.pop(top)
                    top-=1
            print('END')


def main():
    """
    list = LinkedList()
    cont = True
    while cont:
        choice = input('Enter\n0: exit\n1: insert\n2: delete\n')
        if choice == '0':
            cont = False
        if choice == '1':
            print('Enter space seprated info and position:')
            info, pos = map(str, input().split())
            list.insert(info=info, pos=int(pos))
        if choice == '2':
            pos = input('Enter position:')
            list.delete(pos=int(pos))
    """
    """
    cqueue = CircularQueue(int(input('Circular Queue Size:')))
    cont = True
    while cont:
        choice = input('Enter\n0: exit\n1: insert\n2: delete\n')
        if choice == '0':
            cont = False
        if choice == '1':
            cqueue.enqueue(input('Value: '))
        if choice == '2':
            cqueue.dequeue()
    """
    """
    sorting = Sorting(list(map(int, input('Enter Array to sort: ').split())))
    print("Sorted Array:", sorting.merge())
    print("Sorted Array:", sorting.shell(sorting.list.copy()))
    print("Sorted Array:", sorting.quick(sorting.list.copy(), len(sorting.list.copy())-1))
    """
    """
    searching = Searching(list(map(int, input('Enter Array to sort: ').split())))
    print("Sorted Array:", searching.list)
    print("Index: ", searching.interpolation(int(input('Value: ')), lb=0, ub=len(searching.list)-1))
    """
    """
    heap = Heap()
    cont = True
    while cont:
        choice = input('Enter\n0: exit\n1: insert\n2: delete\nChoice:')
        if choice == '0':
            cont = False
        if choice == '1':
            heap.insert(info=input('Value:'))
        if choice == '2':
            heap.delete()
    """
    """
    avl = AVLTree()
    cont = True
    while cont:
        choice = input('Enter\n0: exit\n1: insert\n2: delete\nChoice:')
        if choice == '0':
            cont = False
        if choice == '1':
            avl.insert(info=int(input('Value:')))
        if choice == '2':
            avl.delete(info=int(input('Value:')))
    """
    """
    graph = Graph()
    cont = True
    while cont:
        choice = input('Enter\n0: exit\n1: insert\n2: BFS\n3: DFS\nChoice:')
        if choice == '0':
            cont = False
        if choice == '1':
            vertice=int(input('Vertice:'))
            neighbours=list(map(int, input('List of Neighbours:').split()))
            for neighbour in neighbours:
                graph.insert(vertice=vertice, neighbour=neighbour)
            graph.show()
        if choice == '2':
            graph.bfs()
        if choice == '3':
            graph.dfs()
    """
    #https://www.geeksforgeeks.org/edit-distance-dp-5/
    #str1=input('String 1:')
    #str2=input('String 2:')
    """
    s1, s2-1 : insert
    s1-1, s2 : delete
    s1-1, s2-1 : replace
    """
    def moves(str1, str2, s1, s2, x, y):
        moves=0
        while s1>=0 and s2>=0:
            if str1[s1]==str2[s2]:
                return moves, s1, s2
            else:
                moves+=1
                s1-=x
                s2-=y
        return moves, s1, s2
    def change(str1, str2, s1, s2):
        count = 0
        while  s1>=0 and s2>=0:
            if str1[s1]!=str2[s2]:
                insert, is1, is2=moves(str1, str2, s1, s2, 0, 1)
                delete, ds1, ds2=moves(str1, str2, s1, s2, 1, 0)
                replace, rs1, rs2=moves(str1, str2, s1, s2, 1, 0)
                if min(insert, delete, replace)==insert:
                    s1, s2 = is1, is2
                elif min(insert, delete, replace)==delete:
                    s1, s2 = ds1,ds2
                elif min(insert, delete, replace)==replace:
                    s1, s2 = rs1, rs2
                count+=min(insert, delete, replace)
            else:
                s1-=1
                s2-=1
        return count
    #print('Least Changes:', change(str1, str2, len(str1)-1, len(str2)-1))

    def change2(str1, str2, s1, s2):
        if s1==0:
            return s2
        if s2==0:
            return s1
        if str1[s1-1]==str2[s2-1]:
            return change2(str1, str2, s1-1, s2-1)
        return 1+min(change2(str1, str2, s1, s2-1), change2(str1, str2, s1-1, s2), change2(str1, str2, s1-1, s2-1))
    #print('Least Changes:', change2(str1, str2, len(str1), len(str2)))

    #https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
    def maxadjsum(list):
        odd=0
        even=0
        i=0
        while i<len(list):
            if i%2==0:
                even+=list[i]
            else:
                odd+=list[i]
            i+=1
        return max(even, odd)
    #print(maxadjsum(list(map(int, input('List:').split()))))

    e = list(map(int, input('Entry:').split()))
    a = []
    i=0
    while i < 2:
        a.insert(i, list(map(int, input('Entry Row '+str(i+1)+':').split())))
        i+=1
    t = []
    i=0
    while i < 2:
        t.insert(i, list(map(int, input('Change Row '+str(i+1)+':').split())))
        i+=1
    x = list(map(int, input('Exit:').split()))

    def minpath(e, a, t, x):
        up = e[0]+a[0][0]
        down = e[1]+a[1][0]

        for i in range(1, len(a[0])):
            up, down = min(up+a[0][i], down+a[1][i]+t[0][i]), min(down+a[1][i], up+a[0][i]+t[1][i])

        return min(up+x[0], down+x[1])
    print(minpath(e,a,t,x))


if __name__ == '__main__':
    main()
