#this is a package / module
# here package name is piaic and genai is a model
# what module consist of ?

import time
class ExecutionTimer:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{self.func.__name__}() took {(end - start) * 1000:.4f}ms")
        return result