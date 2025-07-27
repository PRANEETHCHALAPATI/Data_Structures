class Solution:
    @staticmethod
    def gcd(x, y):
        if y == 0:
            return x
        return Solution.gcd(y, x % y)

    def lcm_array(self, arr):
        MOD = 10**9 + 7
        result = arr[0]
        
        for i in range(1, len(arr)):
            a = result
            b = arr[i]
            gcd_value = self.gcd(a, b)
            result = (result // gcd_value * b) % MOD  # avoid overflow, do division first

        return result

# Example usage
s = Solution()
print(s.lcm_array([2, 7, 3, 9, 4]))  # Output: 252
