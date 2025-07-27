class Solution:
    def check_perfect_number(self, num):
        total = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                total += i
                if i != num // i and i != 1:
                    total += num // i
        return total == num

# Example usage
s = Solution()
print(s.check_perfect_number(28))   # True (1 + 2 + 4 + 7 + 14 = 28)
print(s.check_perfect_number(12))   # False
