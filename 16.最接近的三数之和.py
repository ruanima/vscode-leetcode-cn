#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (40.04%)
# Likes:    203
# Dislikes: 0
# Total Accepted:    29.1K
# Total Submissions: 71K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
#
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # v1 暴力法 超时
        # from itertools import combinations
        # ans = 2 ** 31
        # ret = None
        # for a, b, c in combinations(nums, 3):
        #     tmp = abs(a+b+c-target)
        #     if tmp < ans:
        #         ret = a + b + c
        #         ans = tmp
        # return ret

        nums.sort()
        gap = 2 ** 31
        ans = None
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > target:
                    k -= 1
                else:
                    j += 1
                new_gap = abs(total - target)
                if new_gap < gap:
                    gap = new_gap
                    ans = total
        return ans

if __name__ == "__main__":
    s = Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1)
    print(s)

