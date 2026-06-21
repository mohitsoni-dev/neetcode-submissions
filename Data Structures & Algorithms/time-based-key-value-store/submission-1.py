class TimeMap:
    def __init__(self):
        self.memo = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.memo.setdefault(key, [])
        self.memo[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.memo.get(key, [])
        return self.binary_search(timestamps, timestamp)


    def binary_search(self, timestamps: list[tuple], timestamp: int):
        i = 0
        j = len(timestamps) - 1
        ans = ""
        while i <= j:
            mid = (j-i)//2 + i
            if timestamps[mid][0] <= timestamp:
                ans = timestamps[mid][1]
                i = mid + 1
            else:
                j = mid - 1
        return ans