class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp_s = ''.join(sorted(s))
        temp_t = ''.join(sorted(t))

        if temp_s == temp_t:
            return True
        else:
            return False


def main():
    sol = Solution()
    s = "racecar"
    t = "carrace"
    print(sol.isAnagram(s, t))


if __name__ == '__main__':
    main()
