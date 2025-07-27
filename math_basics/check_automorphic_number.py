class Solution:
    def check_automorphic_number(self, num):
        square = num * num
        count = len(str(num))
        mod = 10 ** count
        return square % mod == num

# Example usage
s = Solution()
print(s.check_automorphic_number(76))   # True (76^2 = 5776 → ends in 76)
print(s.check_automorphic_number(25))   # True (25^2 = 625 → ends in 25)
print(s.check_automorphic_number(7))    # False (7^2 = 49 → does not end in 7)
