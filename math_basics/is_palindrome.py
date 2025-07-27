class Solution:
    def is_palindrome(self, n):
        n1 = n
        rev = 0
        while n != 0:
            temp = n % 10
            rev = rev * 10 + temp
            n = n // 10
        return rev == n1

# Example usage
s = Solution()
print(s.is_palindrome(121))   # True
print(s.is_palindrome(123))   # False
