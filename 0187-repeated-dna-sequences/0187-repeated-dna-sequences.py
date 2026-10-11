class Solution:

  def findRepeatedDnaSequences(self, s: str) -> list[str]:
    n = len(s)
    if n <= 10:
        return []

    char_map = {"A":0, "C":1,"G":2,"T":3}
    seen = set()
    repeated = set()
    
    bitmask = (1 << 20 ) - 1

    mask = 0
    for i in range(10):
        mask = (mask << 2)|char_map[s[i]]
    seen.add(mask)
    for i in range(10 , n):
        mask = ((mask << 2 )|char_map[s[i]])&bitmask

        if mask in seen:
            repeated.add(s[i-9:i+1])
        else:
            seen.add(mask)
    
    return list(repeated)