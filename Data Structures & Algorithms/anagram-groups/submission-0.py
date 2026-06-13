class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_to_str = {}
        str_to_group = {}
        g = 0
        for i in range(0, len(strs)):
            s1 = strs[i]
            if s1 not in str_to_group:
                str_to_group[s1] = g
                group_to_str[g] = [s1]
                g += 1
            else:
                continue
            group_s1 = str_to_group[s1]
            for j in range(i+1, len(strs)):
                s2 = strs[j]
                are_anagrams = self.isAnagram(s1, s2)

                if are_anagrams:
                    group_to_str[group_s1].append(s2)
                    str_to_group[s2] = group_s1
        
        ans = [val for _, val in group_to_str.items()]
        return ans


    """
    group_to_str = {
        0: [act, cat]
        1: [pots, tops, stop]
    }

    str_to_group = {
        act: 0,
        cat: 0,
        pots: 1,
        tops: 1,
        stop: 1,
    }
    """



    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        memo = [0] * 26
        
        for c in s:
            memo[ord(c)-ord('a')] = memo[ord(c)-ord('a')] + 1
        
        for c in t:
            memo[ord(c)-ord('a')] = memo[ord(c)-ord('a')] - 1
        
        for c in memo:
            if c != 0:
                return False
        return True