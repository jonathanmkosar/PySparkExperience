
import timeit

def profile_func(func_test, func_name, num_of_passes=100):
    execution_time = timeit.timeit(func_test, number=num_of_passes)
    print(f"{func_name} Execution time: {execution_time:.6f} seconds")