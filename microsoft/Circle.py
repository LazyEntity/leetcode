class Solution:
    def solution(self, arr):
        idx = 0
        result = 0
        while idx < len(arr) - 1:
            if (arr[idx] + arr[idx + 1]) % 2 == 0:
                result += 1
                idx += 1
            idx += 1

        if idx == len(arr) - 1 and (arr[0] + arr[-1]) % 2 == 0:
            result += 1
        return result


if __name__ == '__main__':
    print(Solution().solution([5, 5, 5, 5, 5, 5]))
