import time


""" Decorator for logs """
def log_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[LOG] Function '{func.__name__}' is done by {end_time - start_time:.4f} sec.")
        return result
    return wrapper