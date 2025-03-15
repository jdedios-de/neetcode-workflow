from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        l = []
        mul = 1

        for num in range(len(nums)):
            for n in range(len(nums)):
                if n != num:
                    mul *= nums[n]
            lst.append(mul)
            mul = 1
        return lst


def main():
    sol = Solution()

    #     Output: [48, 24, 12, 8]
    #     nums = [1, 2, 4, 6]

    #     Output: [0, -6, 0, 0, 0]
    nums = [-1, 0, 1, 2, 3]

    print(sol.productExceptSelf(nums))


if __name__ == '__main__':
    main()
