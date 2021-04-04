def fibonacci(input_value):
    if input_value == 1:
        return 1
    elif input_value == 2:
        return 1
    elif input_value > 2:
        return fibonacci(input_value -1) + fibonacci(input_value -2)

def total_runtime():
    import time
    start = time.time()
    fibonacci(40)
    end = time.time()
    print(f"This function took {end-start} seconds to finish")


if __name__ == '__main__':
    total_runtime()