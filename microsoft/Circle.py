class Solution:
    def solution(self, arr):
        idx, size, result = 0, len(arr), 0
        if (arr[0] + arr[-1]) % 2 == 0:
            idx, size, result = 1, size - 1, 1
        while idx < size - 1:
            if (arr[idx] + arr[idx + 1]) % 2 == 0:
                result += 1
                idx += 1
            idx += 1
        return result


if __name__ == '__main__':
    print(Solution().solution([5, 5, 5]))
