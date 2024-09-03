#PROCESS SCHEDULER
import heapq

class Solution:
    def getMinCores(self, start, end):
        n = len(start)
        intervals = list(zip(start, end))
        
        # Sort intervals by start time
        intervals.sort()

        count = 0
        heap = []  # This will store the end times of current tasks
        
        for begin, finish in intervals:
            # Remove all tasks that have ended
            while heap and heap[0] < begin:
                heapq.heappop(heap)
            
            # Add the current task's end time to the heap
            heapq.heappush(heap, finish)
            
            # Update the maximum number of concurrent tasks
            count = max(count, len(heap))
        
        return count

if __name__ == '__main__':
    obj = Solution()
    print(obj.getMinCores([1, 3, 4], [3, 5, 6]))  # Expected output: 2
    print(obj.getMinCores([1, 2, 3], [3, 3, 5]))  # Expected output: 3
    print(obj.getMinCores([1, 4, 7], [2, 4, 10]))  # Expected output: 1
