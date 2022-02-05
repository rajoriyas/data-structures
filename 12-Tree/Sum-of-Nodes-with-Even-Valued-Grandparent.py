# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, tree, array={}, init=True, i=0):
        if init:
            array[i]=tree.val
            init=False
        if tree.left is not None:
            array[2*i + 1]=tree.left.val
            array=self.inorderTraversal(tree.left, array, init, 2*i+1)
        if tree.right is not None:
            array[2*i + 2]=tree.right.val
            array=self.inorderTraversal(tree.right, array, init, 2*i+2)
        return array

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        array=self.inorderTraversal(root)
        i=0
        total=0
        while i<sorted(array.keys())[-1]:
            if array.get(i) is not None and array[i]%2==0:
                if array.get(2*(2*i+1)+1) is not None:
                    total+=array[2*(2*i+1)+1]
                if array.get(2*(2*i+2)+1) is not None:
                    total+=array[2*(2*i+2)+1]
                if array.get(2*(2*i+1)+2) is not None:
                    total+=array[2*(2*i+1)+2]
                if array.get(2*(2*i+2)+2) is not None:
                    total+=array[2*(2*i+2)+2]
            i+=1
        return total
        
