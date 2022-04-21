from collections import defaultdict
import heapq as heap


# From https://levelup.gitconnected.com/dijkstra-algorithm-in-python-8f0e75e3f16e
def dijkstra(G, startingNode):
    visited = set()
    parentsMap = {}
    pq = []
    nodeCosts = defaultdict(lambda: float('inf'))
    nodeCosts[startingNode] = 0
    heap.heappush(pq, (0, startingNode))

    while pq:
        # go greedily by always extending the shorter cost nodes first
        _, node = heap.heappop(pq)
        visited.add(node)

        for adjNode, weight in G[node].items():
            if adjNode in visited: continue

            newCost = nodeCosts[node] + weight
            if nodeCosts[adjNode] > newCost:
                parentsMap[adjNode] = node
                nodeCosts[adjNode] = newCost
                heap.heappush(pq, (newCost, adjNode))

    return parentsMap, nodeCosts


def map_to_graph(levels):
    length = len(levels)
    width = len(levels[0])
    graph = {}
    for i in range(len(levels)):
        for j in range(len(levels[0])):
            node = (i, j)
            graph[node] = {}
            if j < width - 1:
                graph[node][(i, j+1)] = levels[i][j + 1]
            if j > 0:
                graph[node][(i, j-1)] = levels[i][j - 1]
            if i < length - 1:
                graph[node][(i+1, j)] = levels[i + 1][j]
            if i > 0:
                graph[node][(i-1, j)] = levels[i - 1][j]
    return graph


risks = []
with open('day15.txt', 'r') as f:
    for line in f:
        risks.append([int(i) for i in line.rstrip()])

graph_1 = map_to_graph(risks)

distances = dijkstra(graph_1, (0, 0))
M_1 = len(risks)
N_1 = len(risks[0])
print("Part 1:", distances[1][(N_1-1, M_1-1)])

for p in range(N_1):
    for q in range(1, 5):
        risks[p].extend([(i + q) % 9 or 9 for i in risks[p][0:N_1]])

for q in range(1, 5):
    for p in range(M_1):
        risks.append([(i + q) % 9 or 9 for i in risks[p]])

graph_2 = map_to_graph(risks)
distances = dijkstra(graph_2, (0, 0))
M_2 = len(risks)
N_2 = len(risks[0])
print("Part 2:", distances[1][(N_2-1, M_2-1)])
