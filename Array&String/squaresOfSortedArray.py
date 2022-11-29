# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Java sort 

# class Solution {
#     public int[] sortedSquares(int[] A) {
#         int N = A.length;
#         int[] ans = new int[N];
#         for (int i = 0; i < N; ++i)
#             ans[i] = A[i] * A[i];

#         Arrays.sort(ans);
#         return ans;
#     }
# } 

#python
# class Solution(object):
#     def sortedSquares(self, A):
#         return sorted(x*x for x in A)


# Java pointer 
# class Solution {
#     public int[] sortedSquares(int[] nums) {
#         int n = nums.length;
#         int[] result = new int[n];
#         int left = 0;
#         int right = n - 1;

#         for (int i = n - 1; i >= 0; i--) {
#             int square;
#             if (Math.abs(nums[left]) < Math.abs(nums[right])) {
#                 square = nums[right];
#                 right--;
#             } else {
#                 square = nums[left];
#                 left++;
#             }
#             result[i] = square * square;
#         }
#         return result;
#     }
# }



# python pointer 


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result