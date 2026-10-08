class Solution:

  def findRepeatedDnaSequences(self, s: str) -> list[str]:
    n = len(s)
    if n <= 10:
      return []

    # Map nucleotides to 2-bit integers
    char_map = {"A": 0, "C": 1, "G": 2, "T": 3}

    seen = set()
    repeated = set()

    # 20-bit mask (0xFFFFF or (1 << 20) - 1) to keep only last 20 bits
    bitmask = (1 << 20) - 1

    mask = 0
    # First 10 characters ka bitmask banao
    for i in range(10):
      mask = (mask << 2) | char_map[s[i]]
    seen.add(mask)

    # Sliding window with Bitwise Shift
    for i in range(10, n):
      # Left shift 2 bits, add new char, mask to 20 bits
      mask = ((mask << 2) | char_map[s[i]]) & bitmask

      if mask in seen:
        repeated.add(s[i - 9 : i + 1])
      else:
        seen.add(mask)

    return list(repeated)