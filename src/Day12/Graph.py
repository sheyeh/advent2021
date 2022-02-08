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

    def count(self, source='start', visited=None):
        if source == 'end':
            return 1
        if visited is None:
            visited = []
        num_paths = 0
        neighbors = set(self._graph.get(source)) - set(visited)
        for nxt in neighbors:
            next_visited = visited.copy()
            if source.islower():
                next_visited.append(source)
            num_paths += self.count(nxt, next_visited)
        return num_paths
