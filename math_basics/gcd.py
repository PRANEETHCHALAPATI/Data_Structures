class Solution:
    def gcd(self, A, B):
        a = A
        b = B
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return b if a == 0 else a

# Example usage
s = Solution()
print(s.gcd(48, 18))  # Output: 6
