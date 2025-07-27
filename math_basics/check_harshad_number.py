class Solution:
    def check_harshad_number(self, num):
        n1 = num
        digit_sum = 0
        while num != 0:
            digit_sum += num % 10
            num //= 10
        return n1 % digit_sum == 0

# Example usage
s = Solution()
print(s.check_harshad_number(18))  # True (18 / (1 + 8) = 2)
print(s.check_harshad_number(19))  # False
