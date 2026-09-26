class Solution:

  def circularArrayLoop(self, nums: list[int]) -> bool:
    n = len(nums)

    def get_next(curr: int, is_forward: bool) -> int:
      direction = nums[curr] > 0
      # Direction change match check
      if direction != is_forward:
        return -1

      next_idx = (curr + nums[curr]) % n

      # Self loop (length 1) check
      if next_idx == curr:
        return -1

      return next_idx

    global_visited = set()

    for i in range(n):
      if i in global_visited:
        continue

      is_forward = nums[i] > 0
      slow = i
      fast = i
      current_path = set()

      while True:
        # Current path and global visited track karo
        current_path.add(slow)
        global_visited.add(slow)

        slow = get_next(slow, is_forward)
        fast = get_next(fast, is_forward)

        if fast != -1:
          fast = get_next(fast, is_forward)

        # Invalid path (direction mismatch ya self-loop)
        if slow == -1 or fast == -1:
          break

        # Cycle found in the current traversal path!
        if slow in current_path:
          return True

    return False