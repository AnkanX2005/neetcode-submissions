class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])    
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''

        values = self.store[key]
        l = 0
        r = len(values)-1

        ans = ''

        while l <= r:
            mid = (l+r)//2

            current_time = values[mid][1]
            current_val = values[mid][0]

            if current_time == timestamp:
                return current_val
            elif current_time < timestamp:
                ans = current_val
                l = mid + 1
            else:
                r = mid - 1

        return ans                    
        
