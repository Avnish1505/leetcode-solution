from collections import defaultdict


class Solution:

  def maximumSubarraySum(self, nums: list[int], k: int) -> int:
    max_sum = 0
    current_sum = 0
    freq_map = defaultdict(int)

    left = 0

    for right in range(len(nums)):
      # 1. Incoming element ko window mein add karo
      incoming = nums[right]
      current_sum += incoming
      freq_map[incoming] += 1

      # 2. Window size overflow handle karo (size > k)
      if right - left + 1 > k:
        outgoing = nums[left]
        current_sum -= outgoing
        freq_map[outgoing] -= 1

        # Agar frequency 0 ho gayi, map se key delete kar do
        if freq_map[outgoing] == 0:
          del freq_map[outgoing]

        left += 1

      # 3. Exact k-length window check: Agar saare elements distinct hain
      if right - left + 1 == k and len(freq_map) == k:
        max_sum = max(max_sum, current_sum)

    return max_sum