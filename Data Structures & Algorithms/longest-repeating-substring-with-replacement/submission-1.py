class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        i = 0
        j = 0
        ans = 0

        freq = {}
        top_freq = 0

        while i <= j and j < n:
            freq.setdefault(s[j], 0)
            freq[s[j]] = 1 + freq[s[j]]
            if freq[s[j]] > top_freq:
                top_freq = freq[s[j]]

            replacements = (j-i+1) - top_freq

            if replacements <= k:
                ans = max(ans, j-i+1)
                j += 1
            else:
                freq[s[i]] = freq[s[i]] - 1
                freq[s[j]] -= 1
                i += 1
                if i > j:
                    j = i
        
        return ans
                
"""
k = 1
ans = 0
top_c = A
cache = {
    A: 1
}
"AABABBA"
 i
 j
"""