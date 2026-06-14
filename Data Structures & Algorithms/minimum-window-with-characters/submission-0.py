class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        freq2 = {}

        for c in t:
            freq2[c] = freq2.get(c, 0) + 1

        freq1 = {}

        i = 0
        j = 0

        freq1[s[0]] = 1
        min_len = 2000
        ans = None

        while i <= j and j < n:
            while not self.is_valid(freq1, freq2) and j < n - 1:
                j += 1
                freq1[s[j]] = freq1.get(s[j], 0) + 1

            if not self.is_valid(freq1, freq2):
                break

            if (j - i + 1) < min_len:
                min_len = j - i + 1
                ans = s[i:j + 1]

            while freq1.get(s[i], 0) > freq2.get(s[i], 0):
                freq1[s[i]] -= 1
                i += 1

                if (j - i + 1) < min_len:
                    min_len = j - i + 1
                    ans = s[i:j + 1]
            freq1[s[i]] -= 1
            i += 1

        return "" if not ans else ans

    """
min_len = 5
ans = ZODYX
freq2 = {
X: 1
Y: 1
Z: 1
}

freq1 = {
O: 1
U: 0
Z: 1
X: 1
Y: 1
D: 1
}

s="OUZODYXAZV"
      i
         j
    """

    def is_valid(self, freq1: dict, freq2: dict):
        for c in freq2:
            if freq1.get(c, 0) < freq2[c]:
                return False
        return True