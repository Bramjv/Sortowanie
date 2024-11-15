import random
import time


def random_table():
    size = 20000
    min_value = 0
    max_value = 100

    return [random.randint(min_value, max_value) for x in range(size)]


def measure_time(sort_function, lst):
    start_time = time.time()
    sort_function(lst)
    end_time = time.time()
    return end_time - start_time