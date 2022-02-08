from Graph import Graph

graph = Graph()


def count(source='start', visited=None):
    if source == 'end':
        return 1
    if visited is None:
        visited = []
    num_paths = 0
    neighbors = set(graph.get(source)) - set(visited)
    for nxt in neighbors:
        next_visited = visited.copy()
        if source.islower():
            next_visited.append(source)
        num_paths += count(nxt, next_visited)
    return num_paths


with open('day12.txt', 'r') as f:
    for edge in f:
        ends = edge.rstrip().split("-")
        fromNode = ends[0]
        toNode = ends[1]
        graph.add(fromNode, toNode)

print("Part 1:", count())
