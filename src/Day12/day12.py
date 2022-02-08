from Graph import Graph

graph = Graph()


with open('day12.txt', 'r') as f:
    for edge in f:
        ends = edge.rstrip().split("-")
        fromNode = ends[0]
        toNode = ends[1]
        graph.add(fromNode, toNode)

print("Part 1:", graph.count())
