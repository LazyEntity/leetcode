class Solution:
    def getMaximumJobs(self, n, m, k):
        r = m // n + 1
        if m % n > 1:
            r += 1
        return r

if __name__ == '__main__':
    print(Solution().getMaximumJobs(3, 6, 100))
    print(Solution().getMaximumJobs(3, 7, 100))
    print(Solution().getMaximumJobs(3, 8, 100))
    print(Solution().getMaximumJobs(3, 9, 100))
