import heapq


class Solution:
    def getMaximumRewardPoints(self, n, k, arr1, arr2):
        sorted_indexes = sorted([i for i in range(0, n)], key=lambda i: arr1[i] - arr2[i], reverse=True)
        result = 0
        for i in range(0, k):
            result += arr1[sorted_indexes[i]]
        for i in range(k, n):
            result += arr2[sorted_indexes[i]]
        return result

if __name__ == '__main__':
    print(Solution().getMaximumRewardPoints(5, 3, [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]))
    print(Solution().getMaximumRewardPoints(4, 1, [1,2,1,1], [1,1,1,1]))
    print(Solution().getMaximumRewardPoints(5, 1, [1,1,2,3,9], [2,1,1,1,1]))