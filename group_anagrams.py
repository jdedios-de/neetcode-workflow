from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_string = sorted(strs)
        dict_grouping = defaultdict(list)
        return_list = []

        for i in range(len(sorted_string)):
            tmp_str = ''.join(sorted(sorted_string[i]))
            dict_grouping[tmp_str].append(sorted_string[i])

        for value in dict_grouping.values():
            return_list.append(value)
        return return_list


def main():
    sol = Solution()
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(sol.groupAnagrams(strs))


if __name__ == '__main__':
    main()
