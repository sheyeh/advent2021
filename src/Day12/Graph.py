class Graph:

    def __init__(self, graph=None):
        if graph is None:
            graph = {}
        self._graph = graph.copy()

    def _add(self, x, y):
        if self._graph.get(x):
            self._graph[x].append(y)
        else:
            self._graph[x] = [y]

    def add(self, x, y):
        self._add(x, y)
        self._add(y, x)

    def get(self, node):
        return self._graph[node]
