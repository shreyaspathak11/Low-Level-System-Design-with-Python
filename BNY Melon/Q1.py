# Given an array, sort the array according to a number of set
# values in the binary representation of those numbers. If two
# elements have the same number of set values, the value which
# occurs first in the input array will come first in the resultant
# array
class Solution:
    def countBits(self, num):
        count = 0
        while num:
            if num&1:
                count+=1
            num>>=1
        return count
    
    def sortArrayBySetBits(self, arr):
        n = len(arr)
        nums =  []
        for i in range(n):
            count = self.countBits(arr[i])
            nums.append([count, i])
        nums.sort()
        ans = []
        for cnt, idx in nums:
            ans.append(arr[idx])
        return ans

if __name__ == "__main__":
    obj = Solution()
    arr1 = [3, 7, 8, 9]
    arr2 = [4, 1, 2, 3, 5]
    print(obj.sortArrayBySetBits(arr1))
    print(obj.sortArrayBySetBits(arr2))