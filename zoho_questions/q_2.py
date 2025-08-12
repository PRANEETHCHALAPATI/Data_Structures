palindromes_list = []
def is_palindrome(str):
    n = len(str)
    for i in range(n):
        if str[i].lower() == str[n-i-1].lower():
            pass 
        else:
            return False
    return True
    
def find_longest_substring(string):
    if is_palindrome(string):
        palindromes_list.append(string)
        return  
    elif string == "":
        return 
    else:
        find_longest_substring(string[1:])
        find_longest_substring(string[:-1])
        
def print_longest(palindromes_list):
    len_list = list(map(len,palindromes_list))
    max_len = max(len_list)
    for i in palindromes_list:
        if len(i) == max_len:
            print("the longest substring which is a palindrome is:")
            print(i)
            return
def main():
    string = input("enter the string:\n")
    find_longest_substring(string) 
    print_longest(palindromes_list)
main()
    


#solution-2 
#TC : O(n^2) and SC :O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str