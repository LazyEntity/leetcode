import math
from collections import defaultdict


class Solution:
    def solution(self, a, b):
        def fill(up, arr):
            for dice in arr:
                if up:
                    dices[6 - dice] += 1
                else:
                    dices[dice - 1] += 1

        distance = sum(a) - sum(b)
        dices = [0] * 6
        fill(distance < 0, a)
        fill(distance > 0, b)

        result, dice_div, distance = 0, 5, abs(distance)
        while distance > 0 and dice_div > 0:
            if dices[dice_div] != 0:
                divisions = math.ceil(distance / dice_div)
                min_div = min(dices[dice_div], divisions)
                result += min_div
                distance -= min_div * dice_div
            dice_div -= 1
        return result if distance <= 0 else -1


if __name__ == '__main__':
    print(Solution().solution([1, 1], [1, 1]))
    # print(Solution().solution([5, 4], [1, 1]))  # 9, 2: 4,3; 5,5
    # print(Solution().solution([2, 3, 1, 1, 2], [5, 4, 2]))  # 9, 11
    # print(Solution().solution([5, 4, 1, 2, 6, 5], [2]))  # 23, 6
    # print(Solution().solution([1, 1], [6, 6, 6]))
