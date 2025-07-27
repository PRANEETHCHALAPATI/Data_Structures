class Solution:
    def product_of_digits(self, num):
        product = 1
        while num != 0:
            product *= num % 10
            num //= 10
        return product

# Example usage
s = Solution()
print(s.product_of_digits(1234))  # Output: 24 (1*2*3*4)
