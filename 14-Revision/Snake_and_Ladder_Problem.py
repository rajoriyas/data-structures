# User function Template for Python3
import math
class Solution:
    def minThrow(self, N, arr):
        visited=[1,]
        queue=[1,]
        moves=[math.inf for _ in range(30)]
        moves[1-1]=0
        while len(queue)>0:
            ptr=queue.pop(0)
            roll=1
            while roll<=6:
                new_ptr=ptr+roll
                if new_ptr not in visited and new_ptr<=30:
                    visited.append(new_ptr)
                    queue.append(new_ptr)
                    if moves[new_ptr-1]>=moves[ptr-1]+1:
                        moves[new_ptr-1]=moves[ptr-1]+1
                    n=0
                    while n<N:
                        if new_ptr==arr[2*n]:
                            print(new_ptr)
                            new_ptr=arr[2*n +1]
                            visited.append(new_ptr)
                            queue.append(new_ptr)
                            if moves[new_ptr-1]>=moves[ptr-1]+1:
                                moves[new_ptr-1]=moves[ptr-1]+1
                        n+=1
                roll+=1
        return moves[30-1]


#{
#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])

        ob = Solution()
        print(ob.minThrow(N, arr))
# } Driver Code Ends
