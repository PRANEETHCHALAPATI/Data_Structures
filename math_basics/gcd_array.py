import math
from functools import reduce

class Solution:
    def gcd(self, N, arr):
        return reduce(math.gcd, arr)

# Example usage
s = Solution()
print(s.gcd(5, [2, 4, 6, 8, 10]))  # Output: 2



class Solution:
    def gcd(self, N, arr):
        result = arr[0]
        for i in range(1, N):
            a = result
            b = arr[i]
            while a != 0 and b != 0:
                if a > b:
                    a = a % b
                else:
                    b = b % a
            result = b if a == 0 else a
        return result

# Example usage
s = Solution()
print(s.gcd(5, [2, 4, 6, 8, 10]))  # Output: 2
