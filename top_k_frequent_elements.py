from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_list = {}

        for num in nums:
            if num in dict_list.keys():
                dict_list[num] += 1
            else:
                dict_list[num] = 1
        sorted_dict = {key: value for key, value in sorted(dict_list.items(), key=lambda x: x[1], reverse=True)}

        return list(sorted_dict.keys())[:k]


def main():
    sol = Solution()
    nums = [7,7]
    k = 1

    print(sol.topKFrequent(nums, k))


if __name__ == '__main__':
    main()
