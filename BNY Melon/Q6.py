#Pythagorean triples

from collections import defaultdict


class Solution:
    def dfs(self, visited, distances, graph, node, distance_index):
        visited.add(node)
        for adj in graph[node]:
            if adj not in visited:
                distances[adj].append(distances[node][distance_index] + 1)
                self.dfs(visited, distances, graph, adj, distance_index)

    def countPythagoreanTriples(self, tree_nodes, tree_from, tree_to, x, y, z):
        graph = defaultdict(list)
        for i in range(tree_nodes - 1):
            graph[tree_from[i]].append(tree_to[i])
            graph[tree_to[i]].append(tree_from[i])

        distances = [[] for _ in range(tree_nodes)]
        visited = set()
        distances[x].append(0)
        self.dfs(visited, distances, graph, x, 0)

        visited = set()
        distances[y].append(0)
        self.dfs(visited, distances, graph, y, 1)
        
        visited = set()
        distances[z].append(0)
        self.dfs(visited, distances, graph, z, 2)

        count = 0
        for i in range(tree_nodes):
            if i!=x and i!=y and i!=z:
                distances[i].sort()
                if (distances[i][0]**2 + distances[i][1]**2 == distances[i][2]**2):
                    count+=1
        return count

if __name__ == "__main__":
    obj = Solution()
    tree_nodes = 9
    tree_from = [0,1,2,3,4,5,6,7]
    tree_to = [1,2,3,4,5,6,7,8]
    x=3
    y=4
    z=5
    print(obj.countPythagoreanTriples(tree_nodes, tree_from, tree_to, x, y, z))