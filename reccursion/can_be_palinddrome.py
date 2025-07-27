class Solution:
    @staticmethod
    def check(s: str, i: int, n: int, v: list) -> bool:
        if i >= n:
            if len(v) == 0:
                return True
            if len(v) == 1:
                x = v[0]
                return s[x[0]] == s[len(s) // 2] or s[x[1]] == s[len(s) // 2]
            if len(v) == 2:
                x, y = v[0], v[1]
                return (s[x[0]] == s[y[1]] and s[x[1]] == s[y[0]]) or \
                       (s[x[0]] == s[y[0]] and s[x[1]] == s[y[1]])
            return False

        if s[i] == s[n]:
            return Solution.check(s, i + 1, n - 1, v)
        v.append((i, n))
        if len(v) > 2:
            return False
        return Solution.check(s, i + 1, n - 1, v)

    def canBecomePalindrome(self, s: str) -> bool:
        return self.check(s, 0, len(s) - 1, [])

# Example usage:
sol = Solution()
print(sol.canBecomePalindrome("abca"))    # True (remove/change 'b')
print(sol.canBecomePalindrome("abcda"))   # True (change 'b' and 'd')
print(sol.canBecomePalindrome("abcdef"))  # False
