from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        to_set = sorted(set(nums))
        list_of_list = []
        set_list = []
        for num in to_set:
            prev_number = num - 1
            if prev_number in nums:
                list_of_list.append(num)
            else:
                if list_of_list:
                    set_list.append(len(list_of_list))
                    list_of_list = []

                list_of_list.append(num)

        set_list.append(len(list_of_list))

        return max(x for x in set_list)


def main():
    sol = Solution()

    # nums = [2, 20, 4, 10, 11, 12, 13, 14, 15, 3, 4, 5]

    # nums = [0,3,2,5,4,6,1,1]

    # nums = [2,20,4,10,3,4,5]

    nums = [0, -1]

    print(sol.longestConsecutive(nums))


if __name__ == '__main__':
    main()
