class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        i = 0
        j = len(s1)-1
        freq1 = [0] * 26 
        freq2 = [0] * 26
        
        for c in s1:
            freq1[ord(c) - ord('a')] += 1

        for k in range(len(s1)):
            freq2[ord(s2[k]) - ord('a')] += 1

        while j < len(s2):
            if freq1 == freq2:
                return True
            freq2[ord(s2[i]) - ord('a')] -= 1
            i += 1
            j += 1
            if j < len(s2):
                freq2[ord(s2[j]) - ord('a')] += 1
        return False
        