import time

class Timer:
    def __init__(self):
        self.start_time = 0 
        self.temp_time = 0 
        self.total_true_time = 0
        self.is_true = False
    
    def set_true(self):
        if not self.is_true:
            self.temp_time = time.time()
            self.is_true = True
    
    def set_false(self):
        if self.is_true:
            elapsed_time = time.time() - self.temp_time
            self.total_true_time += elapsed_time
            self.temp_time = time.time()
            self.is_true = False
    
    def get_true_time(self):
        return self.total_true_time
    
    def get_total_time(self):
        return time.time() - self.start_time

    def start(self):
        self.start_time = time.time()
        self.temp_time = time.time()
