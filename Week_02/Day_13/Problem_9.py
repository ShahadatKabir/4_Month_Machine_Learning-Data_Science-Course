import time

class Timer:
    def __enter__(self):
        self.start_timer = time.perf_counter()
        return self.start_timer

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_timer = time.perf_counter()
        return f"Exact time taken{self.end_timer - self.start_timer}"


with Timer():
    taken_time = sum(range(10))
    print(taken_time)   
