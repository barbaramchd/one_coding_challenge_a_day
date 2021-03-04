"""
933. Number of Recent Calls
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
"""
class RecentCounter:

    def __init__(self):
        self.previous_calls = []

    def ping(self, t: int) -> int:
        self.previous_calls.append(t)
        threshold = t - 3000

        for call in range(len(self.previous_calls)):
            if self.previous_calls[call] >= threshold:
                index = call
                break

        # any number below the threshold can be deleted
        del self.previous_calls[:index]
        return len(self.previous_calls)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)