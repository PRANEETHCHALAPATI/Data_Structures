class Solution:
    def check_armstrong_number(self, num):
        sum_ = 0
        temp = num
        n = len(str(num))  # Number of digits

        while temp != 0:
            digit = temp % 10
            sum_ += digit ** n
            temp //= 10

        return sum_ == num

# Example usage
s = Solution()
print(s.check_armstrong_number(153))  # True (1^3 + 5^3 + 3^3 = 153)
print(s.check_armstrong_number(123))  # False
