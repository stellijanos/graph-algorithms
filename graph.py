from collections import deque, defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def loadEdges(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                u, v = tuple(map(int, line.rstrip().split(' ')))
                self.addEdge(u, v)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def removeEdge(self, u, v):
        self.graph[u].remove(v)

    def getEdges(self):
        return self.graph

    def bfs(self, start):

        result = []

        visited = set()

        queue = [start]

        while len(queue) > 0:
            node = queue.pop(0)
            if node not in visited:
                result.append(node)
                visited.add(node)
                queue += self.graph[node]

    def dfs(self, start):
        result = []

        visited = set()
        stack = [start]

        while len(stack) > 0:
            node = stack.pop()
            if node not in visited:
                result.append(node)
                visited.add(node)
                stack += self.graph[node][::-1]
