import math
from collections import defaultdict


class Solution:
    def solution(self, row):
        els = defaultdict(lambda: (math.inf, -math.inf))
        result = 0
        for i in range(0, len(row) - 1):
            diagram = row[i: i + 2]
            els[diagram] = (min(els[diagram][0], i), max(els[diagram][1], i))
            result = max(result, els[diagram][1] - els[diagram][0])
        return result if result > 0 else -1


if __name__ == '__main__':
    print(Solution().solution("codiliti"))
