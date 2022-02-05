#User function Template for python3

class Solution:
    def toplogicalSorting(self, stack, visited, ptr, graph):
        visited.append(ptr)
        if ptr in graph.keys():
            for neighbour in graph[ptr]:
                if neighbour not in visited:
                    stack, visited=self.toplogicalSorting(stack, visited, neighbour, graph)
        stack.append(ptr)
        return stack, visited

    def findOrder(self,dict, N, K):
        # code here
        graph={}
        i=0
        while i<len(dict)-1:
            word1=dict[i]
            word2=dict[i+1]

            for letter in word1:
                if letter not in graph.keys():
                    graph[letter]=list()

            length=min(len(word1) ,len(word2))
            for l in range(length):
                if word2[l]!=word1[l]:
                    if word2[l] not in graph[word1[l]]:
                        graph[word1[l]].append(word2[l])
                    break
                j+=1
            i+=1
        visited=[]
        stack=[]
        for ptr in graph.keys():
            if ptr not in visited:
                stack, visited=self.toplogicalSorting(stack, visited, ptr, graph)
        return stack[::-1]

#{
#  Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word

    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])

        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
