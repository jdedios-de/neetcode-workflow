from typing import List

SEPARATOR = "#"


class Solution:
    def encode(self, strs: List[str]) -> str:
        temp_list = ""
        for word in strs:
            temp_list += str(len(word)) + SEPARATOR + word
        return temp_list

    def decode(self, s: str) -> List[str]:
        pointer = 0
        return_list = []

        while pointer < len(s):
            if s[pointer + 1] == SEPARATOR:
                start = pointer + 2
                end = int(s[pointer]) + start
                return_list.append(s[start:end])
                pointer = end

        return return_list


def main():
    sol = Solution()
    encoded = sol.encode(["neet","code","love","you"])

    print(sol.decode(encoded))


if __name__ == '__main__':
    main()
