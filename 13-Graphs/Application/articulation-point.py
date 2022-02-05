"""
REF - https://www.geeksforgeeks.org/bridge-in-a-graph/
"""
class Solution:
    def dfs(self, node, graph, visited, intime, lowtime, parents, criticals=[]):
        visited[node]=True
        for neighbour in graph[node]:
            if not visited[neighbour]:
                parents[neighbour]=node
                lowtime[neighbour]=intime[neighbour]=intime[node]+1
                visited, intime, lowtime, parents, criticals=self.dfs(neighbour, graph, visited, intime, lowtime, parents, criticals)
                """
                Checking parent lowtime is higher then chlid lowtime, if yes, changing to equal to it's child
                """
                if lowtime[node]>lowtime[neighbour]:
                    lowtime[node]=lowtime[neighbour]
            else:
                """
                Backtracked Edge
                """
                if intime[neighbour]<lowtime[node] and neighbour!=parents[node]:
                    lowtime[node]=intime[neighbour]
            """
            Checking is neighbour connected via node only?, then it's a critical node
            """
            if lowtime[neighbour]>intime[node]:
                criticals.append([node, neighbour])
        return visited, intime, lowtime, parents, criticals

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph={}
        visited={}
        parents={}
        lowtime={}
        intime={}
        for connect in connections:
            for i in range(2):
                if graph.get(connect[i]) is None:
                    graph[connect[i]]=[connect[1-i],]
                    visited[connect[i]]=False
                    parents[connect[i]]=None
                    lowtime[connect[i]]=1
                    intime[connect[i]]=1
                else:
                    graph[connect[i]].append(connect[1-i])
        criticals=[]
        visited, intime, lowtime, parents, criticals=self.dfs(list(graph.keys())[0], graph, visited, intime, lowtime, parents)
        return criticals
"""
class Solution:
    def dfs(self, vertex, graph, visited, intime, lowtime, parents, criticals=[]):
        for node, neighbours in graph.items():
            if node==vertex:
                visited[node]=True
                for neighbour in neighbours:
                    if not visited[neighbour]:
                        parents[neighbour]=node
                        lowtime[neighbour]=intime[neighbour]=intime[node]+1
                        visited, intime, lowtime, parents, criticals=self.dfs(neighbour, graph, visited, intime, lowtime, parents, criticals)
                        """
                        Checking parent lowtime is higher then chlid lowtime, if yes, changing to equal to it's child
                        """
                        if lowtime[node]>lowtime[neighbour]:
                            lowtime[node]=lowtime[neighbour]
                    else:
                        """
                        Backtracked Edge
                        """
                        if intime[neighbour]<lowtime[node] and neighbour!=parents[node]:
                            lowtime[node]=intime[neighbour]
                    """
                    Checking is neighbour connected via node only?, then it's a critical node
                    """
                    if lowtime[neighbour]>intime[node]:
                        criticals.append([node, neighbour])
        return visited, intime, lowtime, parents, criticals

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph={}
        visited={}
        parents={}
        lowtime={}
        intime={}
        for connect in connections:
            for i in range(2):
                if graph.get(connect[i]) is None:
                    graph[connect[i]]=[connect[1-i],]
                    visited[connect[i]]=False
                    parents[connect[i]]=None
                    lowtime[connect[i]]=1
                    intime[connect[i]]=1
                else:
                    graph[connect[i]].append(connect[1-i])
        criticals=[]
        visited, intime, lowtime, parents, criticals=self.dfs(list(graph.keys())[0], graph, visited, intime, lowtime, parents)
        return criticals
"""
"""
class Solution:
    def getNeighbour(self, connections, visited, stack, parent, intime, lowtime):
        targetNode=stack[-1]
        next=None
        for connection in connections:
            i=0
            while i<2:
                currNode=connection[i]
                nextNode=connection[1-i]
                if targetNode==currNode:
                    if not visited[nextNode]:
                        visited[nextNode]=True
                        next=nextNode
                        stack.append(nextNode)
                        parent[nextNode]=currNode

                        intime[nextNode]+=intime[currNode]+1
                        lowtime[nextNode]=intime[nextNode]
                        return stack, visited, next, parent, intime, lowtime
                    else:
                        if lowtime[currNode]>intime[nextNode] and nextNode!=parent[currNode]:
                            lowtime[currNode]=intime[nextNode]
                i+=1
        return stack, visited, next, parent, intime, lowtime

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        if len(connections)>1:
            criticalConnections=[]
            visited=dict()
            intime=dict()
            lowtime=dict()
            parent=dict()
            for connection in connections:
                visited[connection[0]]=False
                visited[connection[1]]=False

                intime[connection[0]]=0
                intime[connection[1]]=0

                lowtime[connection[0]]=0
                lowtime[connection[1]]=0

                parent[connection[0]]=None
                parent[connection[1]]=None
            stack=[connections[0][0],]
            visited[connections[0][0]]=True
            intime[connections[0][0]]=1
            lowtime[connections[0][0]]=1
            next=None
            while len(stack)>0:
                stack, visited, next, parent, intime, lowtime=self.getNeighbour(connections, visited, stack, parent, intime, lowtime)
                if next is None:
                    child=stack.pop()
                    if len(stack)>0:
                        parentNode=stack[-1]
                        if lowtime[child]<lowtime[parentNode]:
                            lowtime[parentNode]=lowtime[child]
                        parentNode=parent[child]
                        if intime[parentNode]<lowtime[child]:
                            criticalConnections.append([parentNode, child])
        else:
            criticalConnections=connections
        return criticalConnections
"""
"""
class Solution:
    def dfs(self, vertex, connections, visited={}, intime={}, lowtime={}, parents={}, criticals=[]):
        for connect in connections:
            i=0
            while i<2:
                u=connect[i]
                v=connect[1-i]
                if intime.get(u) is None:
                    intime[u]=1
                    lowtime[u]=intime[u]
                    parents[u]=None
                if visited.get(v) is None:
                    visited[v]=False
                if u==vertex:
                    if not visited[v]:
                        visited[u]=True
                        visited[v]=True
                        intime[v]=intime[u]+1
                        lowtime[v]=intime[v]
                        parents[v]=u
                        visited, intime, lowtime, parents, criticals=self.dfs(connect[1-i], connections, visited, intime, lowtime, parents, criticals)
                        if lowtime[u]>lowtime[v]:
                            lowtime[u]=lowtime[v]
                    else:
                        if lowtime[u]>intime[v] and v!=parents[u] and u!=parents[v]:
                            lowtime[u]=intime[v]
                    if lowtime[v]>intime[u]:
                        criticals.append(connect)
                i+=1
        return visited, intime, lowtime, parents, criticals

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        criticals=[]
        _, _, _, _, criticals=self.dfs(connections[0][0], connections)
        return criticals
"""
