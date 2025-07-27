class Solution:
    def sqrt_newton(self, S, precision=1e-6):
        if S < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        if S == 0 or S == 1:
            return S

        x = S / 2.0  # Initial guess

        while abs(x * x - S) > precision:
            x = 0.5 * (x + S / x)

        return x

# Example usage
s = Solution()
print(s.sqrt_newton(25))       # Output: approx. 5.0
print(s.sqrt_newton(2))        # Output: approx. 1.4142...
print(s.sqrt_newton(0))        # Output: 0
