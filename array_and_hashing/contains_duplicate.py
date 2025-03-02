from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_list = set(nums)

        if len(temp_list) == len(nums):
            return False
        else:
            return True


def main():
    sol = Solution()
    nums = [1, 2, 3, 3]
    print(sol.hasDuplicate(nums))


if __name__ == '__main__':
    main()
