# Potential attack vectors
import math

class Solution:
    def getNumVectors(self, keys, queries):
        q = len(queries)
        vector = []
        for query in queries:
            count = 0
            for i in range(len(query)):
                x = query[i]
                n = 0
                for key in keys:
                    if key%x == 0:
                        n+=1
                if n==1:
                    count += 1
                else:
                    count += n + math.factorial(n)
            vector.append(count)
        return vector   
    
      
if __name__ == "__main__":
    keys = [6,9,10] 
    queries = [[2,3],[9,10]]
    obj = Solution()
    ans = obj.getNumVectors(keys, queries)
    print(ans)
