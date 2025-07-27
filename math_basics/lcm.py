class Solution:
    def lcm(self, A, B):
        x, y = A, B
        a, b = A, B

        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a

        gcd = b if a == 0 else a
        return (x * y) // gcd

# Example usage
s = Solution()
print(s.lcm(12, 15))  # Output: 60
