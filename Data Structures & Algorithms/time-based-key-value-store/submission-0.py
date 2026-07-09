class TimeMap:

    def __init__(self):
        self.key_value_pair = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value_pair[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        value = self.key_value_pair.get(key, [])
        if not value:
            return ""
        left = 0
        right = len(value)-1
        while left < right-1:
            mid = left + (right-left)//2

            if value[mid][1] <= timestamp:
                left = mid
            elif value[mid][1] > timestamp:
                right = mid-1

        if value[right][1] <= timestamp:
            return value[right][0]
        elif value[left][1] <= timestamp:
            return value[left][0]
        else:
            return ""
        
