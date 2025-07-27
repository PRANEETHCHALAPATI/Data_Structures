class Solution:
    def second_largest_digit(self, num):
        digits = set()
        while num != 0:
            digits.add(num % 10)
            num //= 10

        if len(digits) < 2:
            return -1

        sorted_digits = sorted(digits, reverse=True)
        return sorted_digits[1]

# Example usage
s = Solution()
print(s.second_largest_digit(98543))  # Output: 8
print(s.second_largest_digit(1111))   # Output: -1
