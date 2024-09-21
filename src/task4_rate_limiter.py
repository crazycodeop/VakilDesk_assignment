import time
from collections import deque
from threading import Lock

class RateLimiter:
    def __init__(self, max_requests=5, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.user_requests = {}
        self.lock = Lock()

    def allow_request(self, user_id):
        with self.lock:
            current_time = time.time()
            if user_id not in self.user_requests:
                self.user_requests[user_id] = deque()

            requests = self.user_requests[user_id]

            while requests and requests[0] <= current_time - self.time_window:
                requests.popleft()

            if len(requests) < self.max_requests:
                requests.append(current_time)
                return True
            else:
                return False

if __name__ == "__main__":
    limiter = RateLimiter(max_requests=5, time_window=60)
    
    # test requests
    for i in range(10):
        user_id = "user1"
        if limiter.allow_request(user_id):
            print(f"Request {i+1} allowed for {user_id}")
        else:
            print(f"Request {i+1} denied for {user_id}")
        # some delay
        time.sleep(0.1)