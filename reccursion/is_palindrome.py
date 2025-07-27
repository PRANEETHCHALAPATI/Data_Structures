class Solution:
    @staticmethod
    def check(s: str, i: int, N: int) -> bool:
        if i >= N // 2:
            return True
        if s[i] != s[N - i - 1]:
            return False
        return Solution.check(s, i + 1, N)

    def checkPalindrome(self, s: str) -> bool:
        return self.check(s, 0, len(s))

# Example usage:
sol = Solution()
print(sol.checkPalindrome("madam"))  # Output: True
print(sol.checkPalindrome("hello"))  # Output: False
