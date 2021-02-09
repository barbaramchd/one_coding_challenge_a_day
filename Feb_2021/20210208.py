"""
125. Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""
# SOLUTION 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = "".join([i if 48 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 else '' for i in s]).lower()
        if len(s_new)%2 == 0:
            print("even: ", s_new)
            for char in range (len(s_new)):
                if s_new[char] != s_new[-(1+char)]:
                    print("even2: ", s_new[char], s_new[-(1+char)])
                    return False
        else:
            print("odd: ", s_new)
            for char in range (len(s_new)//2):
                if s_new[char] != s_new[-(1+char)]:
                    print("odd2: ", s_new[char], s_new[-(1+char)])
                    return False
        return True