class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # max freq = len(nums)
        # min freq = 1

        freq = [[] for _ in range(len(nums)+1)]

        f = {}

        for num in nums:
            if num not in f:
                f[num] = 0
            f[num] = 1 + f[num]

        for num, count in f.items():
            freq[count].append(num)


        res = []

        i = len(freq)-1
        while i >= 0 and len(res) < k:
            ls = freq[i]
            j = 0
            while j < len(ls) and len(res) < k:
                res.append(ls[j])
                j += 1
            i -= 1

        return res

"""
f = {
1: 1,
2: 2,
3: 3
}

freq = [[], [1], [2], [3], [], [], []]
"""