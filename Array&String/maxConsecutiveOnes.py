# Given a binary array, find the maximum number of consecutive 1s in this array.



# Java 
#
# class Solution {
#     public int findMaxConsecutiveOnes(int[] nums) {
#         Hint: Initialise and declare a variable here to 
#         keep track of how many 1's you've seen in a row.
#         int maxNum = 0, max;
                # for(int n, nums)
                #     max = Math.max(max, maxNum = n == 0 ? 0: maxNum++)
                # return max
#     }
# }

# class Solution {
#   public int findMaxConsecutiveOnes(int[] nums) {
#     int count = 0;
#     int maxCount = 0;
#     for(int i = 0; i < nums.length; i++) {
#       if(nums[i] == 1) {
#          Increment the count of 1's by one.
#         count += 1;
#       } else {
#         Find the maximum till now.
#         maxCount = Math.max(maxCount, count);
#         Reset count of 1.
#         count = 0;
#       }
#     }
#     return Math.max(maxCount, count);
#   }
# }



# python

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                # Increment the count of 1's by one.
                count += 1
            else:
                # Find the maximum till now.
                max_count = max(max_count, count)
                # Reset count of 1.
                count = 0
        return max(max_count, count)