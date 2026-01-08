import time

class RateLimiter:
    def __init__(self):
        self.timestamps = []

    def allow(self) -> bool:
        # TODO
        requests_in_window = 0
        now = time.time()
        for t in self.timestamps[-3:]:
            if t > (now - 5):
                requests_in_window += 1
        if requests_in_window >= 3:
            return False
        
        self.timestamps.append(time.time())
        return True


rl = RateLimiter()

for _ in range(3):
    print(rl.allow())

print(rl.allow())  # should be False

time.sleep(5)

print(rl.allow())  # should be True
