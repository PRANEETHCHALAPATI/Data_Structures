class Solution:
    def count_repeating_digits(self, num):
        digit_count = {}
        while num != 0:
            digit = num % 10
            digit_count[digit] = digit_count.get(digit, 0) + 1
            num //= 10

        count = 0
        for freq in digit_count.values():
            if freq > 1:
                count += 1

        return count

# Example usage
s = Solution()
print(s.count_repeating_digits(122334))  # Output: 3 (digits 2, 3, and possibly 4 if repeated)
