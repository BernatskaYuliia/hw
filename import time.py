import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = end_time - start_time
        print(f"Час виконання {func.__name__}: {elapsed_time} секунд")
        return result
    return wrapper


@measure_time 
def example_function():
    time.sleep(2)

example_function()