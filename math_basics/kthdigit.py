class Solution:
    def kth_digit(self, A, B, k):
        total = A ** B
        for _ in range(k - 1):
            total //= 10
        return total % 10

# Example usage
s = Solution()
print(s.kth_digit(2, 10, 3))  # Example: 2^10 = 1024 → 3rd digit from right is 0
