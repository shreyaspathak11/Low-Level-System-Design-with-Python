#process scheduler
import heapq


class Solution:
    def getMinCores(self, start, end):
        n = len(start)
        count = 0
        heap = []
        for i in range(n):
            begin, finish = start[i], end[i]
            if not heap or heap[-1][0] >= begin:
                heapq.heappush(heap, (finish, begin))
                count = max(count, len(heap))
            if heap and heap[i][0] < begin:
                heapq.heappop(heap)
                heapq.heappush(heap, (finish, start))
            
        return count

if __name__ == '__main__':
    obj = Solution()
    print(obj.getMinCores([1,3,4], [3,5,6]))
    print(obj.getMinCores([1,2,3], [3,3,5]))
    print(obj.getMinCores([1,4,7], [2,4,10]))

