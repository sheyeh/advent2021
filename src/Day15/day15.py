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

risks = []
with open('day15.txt', 'r') as f:
    for line in f:
        risks.append([int(i) for i in line.rstrip()])

M = len(risks)
N = len(risks[0])
graph = {}
for i in range(len(risks)):
    for j in range(len(risks[0])):
        node = (i,j)
        graph[node] = {}
        if j < N - 1:
            graph[node][(i, j+1)] = risks[i][j + 1]
        if j > 0:
            graph[node][(i, j-1)] = risks[i][j - 1]
        if i < M - 1:
            graph[node][(i+1, j)] = risks[i + 1][j]
        if i > 0:
            graph[node][(i-1, j)] = risks[i - 1][j]

distances = dijkstra(graph, (0,0))
print("Part 1:",distances[1][(N-1,M-1)])
















