# WALLET DENOMINATION
from collections import Counter
import math


class Solution:
    def findMinDollars(self, arr, n):
        hashmap = Counter(arr)
        max_count =0
        max_val = 0
        # find one with max occurence
        for key, val in hashmap.items():
            if val > max_count:
                max_val = key
                max_count = val
                
        total = 0
        for i in range(n):
            if arr[i] < max_val:
                #need to make arr[i] equal to max_val
                curr_val = arr[i]
                while curr_val < max_val:
                    total += 1
                    if curr_val + 1 <= max_val <= curr_val*2:
                        break
                    curr_val = curr_val*2
            elif arr[i] > max_val:
                # need to make arr[i] equal to max_val
                curr_val = arr[i]
                while curr_val > max_val:
                    total += 1
                    if math.ceil(curr_val/2) <= max_val <= curr_val - 1:
                        break
                    curr_val = math.ceil(curr_val/2)
            
        return total


if __name__ == "__main__":
    arr = [1,2,3,3,5,2]
    n = len(arr)
    obj = Solution()
    ans = obj.findMinDollars(arr, n)
    print(ans)