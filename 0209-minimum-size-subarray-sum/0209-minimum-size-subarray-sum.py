class Solution:

  def minSubArrayLen(self, target: int, nums: list[int]) -> int:
    n = len(nums)
    left = 0
    current_sum = 0
    min_len = float('inf')  # Infinity se initialize kiya

    for right in range(n):
      # 1. Window ko right side se expand karo
      current_sum += nums[right]

      # 2. Jab tak sum >= target hai, window ko left side se shrink karo
      while current_sum >= target:
        # Minimum length update karo
        min_len = min(min_len, right - left + 1)

        # Left element remove karke window narrow karo
        current_sum -= nums[left]
        left += 1

    # Agar min_len change nahi hua (matlab koi valid subarray nahi mila), return 0
    return min_len if min_len != float('inf') else 0