from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash_map.values():
                key = [key for key, value in hash_map.items() if
                       value == difference]
                return [key[0], i]
            else:
                hash_map[i] = nums[i]


def main():
    sol = Solution()
    nums = [3, 4, 5, 6]
    target = 7
    print(sol.twoSum(nums, target))


if __name__ == '__main__':
    main()
