import copy


class Graph:

    def __init__(self, graph=None):
        if graph is None:
            graph = {}
        self._graph = copy.deepcopy(graph)

    def _add(self, x, y):
        if self._graph.get(x):
            self._graph[x].append(y)
        else:
            self._graph[x] = [y]

    def add(self, x, y):
        self._add(x, y)
        self._add(y, x)

    def nodes(self):
        return self._graph.keys()

    def get(self, node):
        return self._graph[node]

    def count(self, source='start', visited=None, path=None, paths=[]):
        if source == 'end':
            path.append(source)
            paths.append(path)
            return 1, paths
        if visited is None:
            visited = []
            path = []
        path.append(source)
        num_paths = 0
        neighbors = set(self._graph.get(source)) - set(visited)
        for nxt in neighbors:
            next_visited = visited.copy()
            if source.islower():
                next_visited.append(source)
            cnt = self.count(nxt, next_visited, path.copy(), paths)[0]
            num_paths += cnt
        return num_paths, paths

    def clone(self):
        return Graph(copy.deepcopy(self._graph))

    def duplicate(self, node):
        dup_node = node + "%"
        neighbors = self._graph.get(node)
        self._graph[dup_node] = neighbors
        for n in neighbors:
            self._graph[n].append(dup_node)
        return self
