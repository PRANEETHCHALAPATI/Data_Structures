class Solution:
    def check_even_digits(self, num):
        while num != 0:
            digit = num % 10
            if digit % 2 != 0:
                return False
            num //= 10
        return True

# Example usage
s = Solution()
print(s.check_even_digits(2486))  # True
print(s.check_even_digits(1234))  # False
