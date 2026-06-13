class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            char_freq_1 = [0] * 26
            for c in s:
                char_freq_1[ord(c) - ord('a')] += 1
            k = tuple(char_freq_1)
            if k in groups:
                groups[k].append(s)
            else:
                groups[k] = [s]

        return list(groups.values())