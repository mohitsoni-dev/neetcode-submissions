class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_to_str = {}
        
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in group_to_str:
                group_to_str[ss] = []
            
            group_to_str[ss].append(s)
        
        return [val for _, val in group_to_str.items()]


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