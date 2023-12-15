class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BST:
    def __init__(self):
        self.root = None
    def insert(self,node, num):
        if node is None:
            return TreeNode(num)
        if num < node.val:
            node.left = self.insert(node.left, num)
        elif num > node.val:
            node.right = self.insert(node.right, num)
        return node
    def arrayToBST(self, nums):
        for x in nums:
            self.root = self.insert(self.root,x)
if __name__ == '__main__':
    

    
        
