from Graph import Graph

graph = Graph()


with open('day12.txt', 'r') as f:
    for edge in f:
        ends = edge.rstrip().split("-")
        fromNode = ends[0]
        toNode = ends[1]
        graph.add(fromNode, toNode)

print("Part 1:", graph.count()[0])

paths_with_duplicates = []
for cave in [cave for cave in set(graph.nodes()) - {'start', 'end'} if cave.islower()]:
    paths_with_duplicates += graph.clone().duplicate(cave).count()[1]

str_paths = set([str(path).replace("%", "") for path in paths_with_duplicates])
print("Part 2:", len(str_paths))
