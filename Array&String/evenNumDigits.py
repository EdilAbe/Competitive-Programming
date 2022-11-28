# Given an array nums of integers, return how many of them contain an even number of digits.

# Constraints:

# 1 <= nums.length <= 500
# 1 <= nums[i] <= 105

# java

# class Solution {
#     public int findNumbers(int[] nums) {
#         int count=0;
#         for(int i=0;i<nums.length;i++){
#             if((nums[i]>=10 && nums[i]<100)
#                 || (nums[i]>=1000 && nums[i]<10000  || nums[i]==100000))
#                 count++;
#         }
#         return count;
#     }
# }


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        totalEven = 0
        
        for num in nums:
            if (num > 9 and num < 100) or (num > 999 and num < 10000) or num == 100000:
                totalEven += 1
        return totalEven