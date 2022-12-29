class Solution:
    def solution(self, matrix):
        def check_range(i, j):
            return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

        def find_next_iter(i, j):
            max_val = -1
            max_dirs = []
            for x, y in directions:
                n_i, n_j = i + x, j + y
                if not check_range(n_i, n_j) or used[n_i][n_j] or matrix[n_i][n_j] < max_val:
                    continue
                if max_val < matrix[n_i][n_j]:
                    max_val = matrix[n_i][n_j]
                    max_dirs = [(n_i, n_j)]
                else:
                    max_dirs.append((n_i, n_j))
            return max_dirs

        def rec_search(i, j, idx):
            if idx == 1:
                return matrix[i][j]
            used[i][j] = True
            max_val = -1
            for n_i, n_j in find_next_iter(i, j):
                max_value = rec_search(n_i, n_j, idx - 1)
                if max_value >= pow(10, idx - 2):
                    max_val = max(max_val, matrix[i][j] * pow(10, idx - 1) + max_value)
            used[i][j] = False
            return max_val

        if len(matrix) == 1:
            max_val = -1
            for i in range(len(matrix[0]) - 3):
                max_val = max(max_val,
                              matrix[0][i] * pow(10, 3) + matrix[0][i + 1] * pow(10, 2) + matrix[0][i + 2] * pow(10, 1) + matrix[0][i + 3])
            for i in range(len(matrix[0]) - 1, 2, -1):
                max_val = max(max_val,
                              matrix[0][i] * pow(10, 3) + matrix[0][i - 1] * pow(10, 2) + matrix[0][i - 2] * pow(10, 1) + matrix[0][i - 3])
            return max_val

        directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        used = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        result = -1
        for el in reversed(range(max([max(row) for row in matrix]) + 1)):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if el == matrix[i][j]:
                        result = max(rec_search(i, j, 4), result)
            if result > 0:
                break
        return result


if __name__ == '__main__':
    print(Solution().solution([[1, 1, 1],
                               [1, 3, 4],
                               [1, 4, 3]]))
    print(Solution().solution([[0, 1, 2, 2, 1]]))

    print(Solution().solution([[9, 1, 1, 0, 7],
                               [1, 0, 2, 1, 0],
                               [1, 9, 1, 1, 0]]))
