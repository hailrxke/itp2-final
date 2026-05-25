import time
import functools

""" Decorator for logs """


def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"[LOG] Start: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            print(f"[LOG] Done: {func.__name__} ({time.time() - start:.4f}s)")
            return result
        except Exception as exc:
            print(f"[LOG] Error in {func.__name__}: {exc}")
            raise

    return wrapper

log_action = log_execution