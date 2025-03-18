import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitize_string = ''.join(e for e in s if e.isalnum()).lower()

        for charac in range(len(sanitize_string) // 2):

            if sanitize_string[charac] != sanitize_string[-(charac + 1)]:
                return False

        return True


def main():
    sol = Solution()
    #s = "Was it a car or a cat I saw?"
    #s = "Madam, in Eden, I'm Adam"
    #s = "tab a cat"
    s = "0P"
    print(sol.isPalindrome(s))


if __name__ == '__main__':
    main()
