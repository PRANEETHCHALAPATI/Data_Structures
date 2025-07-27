class Solution:
    def calculate_digit_sum(self, N1, N2):
        total_sum = 0
        for i in range(N1, N2 + 1):
            temp = i
            while temp != 0:
                total_sum += temp % 10
                temp = temp // 10
        return total_sum

# Example usage
s = Solution()
print(s.calculate_digit_sum(10, 12))  # Output: 6 (1+0 + 1+1 + 1+2)
