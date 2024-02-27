class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.value, end=' ')
            self.inOrder(root.right)

    def preOrder(self, root):
        if root:
            print(root.value, end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.value, end=' ')
