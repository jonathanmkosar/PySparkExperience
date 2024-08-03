import random
from timeit_helper import profile_func


def linear_search(arr, x):  # Big O(n)
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


# It returns location of x in given array arr - Big O(log n)
# The data structure must be sorted.
# Access to any element of the data structure should take constant time.
def binary_search(
    arr,
    x,
    low=0,
    high=None,
):
    if not high:
        high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


def main():
    arr = tuple(range(1, 1000000))
    random_num = random.choice(arr)
    print(f"Random Number: {random_num}")
    func_maps = {
        "linear_search": linear_search,
        "binary_search": binary_search,
    }
    for func_algo, func_test in func_maps.items():
        profile_func(lambda: func_test(arr, random_num), func_algo, 100)


if __name__ == "__main__":
    main()
    
