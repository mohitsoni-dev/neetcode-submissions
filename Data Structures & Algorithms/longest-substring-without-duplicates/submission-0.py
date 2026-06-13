class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0

        n = len(s)
        i = 0
        j = 0

        cache = dict()

        while i <= j and j < n:
            if s[j] in cache:
                pos = cache.get(s[j])
                while i <= pos and i < j:
                    del cache[s[i]]
                    i += 1
            cache[s[j]] = j
            max_len = max(max_len, j-i+1)
            j += 1
        
        return max_len
"""
max_len = 3
pos = 0
"abcabcbb"
  i
    j
cache = {
    b: 1,
    c: 2,
    a: 3
}
"""