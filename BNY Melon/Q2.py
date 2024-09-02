from collections import defaultdict
import heapq

class Solution():
    def __init__(self) -> None:
        self.not_path = set()

    def findAnswer(self, n, m, t, endpoint1, endpoint2, edgeLength):
        graph = defaultdict(list)
        for i in range(m):
            graph[endpoint1[i]].append([endpoint2[i], edgeLength[i]])
            graph[endpoint2[i]].append([endpoint1[i], edgeLength[i]])
        
        ans = [-1 for _ in range(n)]
        ans[0] = 0  # Starting node has a distance of 0
        for i in range(1, n + 1):
            if i in self.not_path:
                continue
            distance = self.dijkstra(i, graph)
            if distance == -1 or distance >= t[i - 1]:
                self.not_path.add(i)
            else:
                ans[i - 1] = distance
        return ans

    def dijkstra(self, dest, graph):
        heap = []
        heapq.heappush(heap, (0, 1))  # Start from node 1 with distance 0
        visited = set()
        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if node == dest:
                return dist
            for adj, wt in graph[node]:
                if adj not in visited and adj not in self.not_path:
                    heapq.heappush(heap, (dist + wt, adj))
        return -1

if __name__ == '__main__':
    obj = Solution()
    n = 4
    m = 4
    t = [1, 2, 7, 9]
    endpoint1 = [1, 2, 3, 4]
    endpoint2 = [2, 4, 1, 3]
    edgeLength = [2, 1, 5, 3]
    print(obj.findAnswer(n, m, t, endpoint1, endpoint2, edgeLength))  # Should output: [0, -1, 5, 8]
