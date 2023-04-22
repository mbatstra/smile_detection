import time

class Timer:
    def __init__(self):
        self.start_times = []
        self.end_times = []

    def start(self):
        self.start_times.append(time.time())

    def stop(self):
        if len(self.start_times) == len(self.end_times) + 1:
            self.end_times.append(time.time())
        else:
            raise Exception("Must call start() before stop()")

    def elapsed(self, n=1):
        if n > len(self.end_times):
            raise Exception("Not enough measurements")
        return self.end_times[-n] - self.start_times[-n]
