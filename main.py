from graph import Graph
from tree_node import TreeNode


def graph():
    g = Graph()
    g.loadEdges('knoten.txt')

    g.bfs(1)
    g.dfs(1)


def treeNode():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(8)
    root.right.left.left = TreeNode(9)
    root.right.right.left = TreeNode(10)
    root.right.right.right = TreeNode(11)

    root.inOrder(root)
    print()
    root.preOrder(root)
    print()
    root.postOrder(root)

def main():
    graph()
    treeNode()

main()
