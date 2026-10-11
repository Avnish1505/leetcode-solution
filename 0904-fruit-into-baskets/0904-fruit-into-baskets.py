from collections import defaultdict


class Solution:

  def totalFruit(self, fruits: list[int]) -> int:
    basket = defaultdict(int)  # Map: fruit_type -> count in window
    left = 0
    max_fruits = 0

    for right in range(len(fruits)):
      # 1. Incoming fruit ko basket mein add karo
      incoming = fruits[right]
      basket[incoming] += 1

      # 2. Agar basket mein 2 se zyada types ke fruits ho gaye, window shrink karo
      while len(basket) > 2:
        outgoing = fruits[left]
        basket[outgoing] -= 1

        # Agar count 0 ho gaya, toh basket se ye fruit type poori tarah hata do
        if basket[outgoing] == 0:
          del basket[outgoing]

        left += 1

      # 3. Valid window (<= 2 types): Max calculation
      max_fruits = max(max_fruits, right - left + 1)

    return max_fruits

    # time complexity = 0(n)
    # space complexit = 0(1)