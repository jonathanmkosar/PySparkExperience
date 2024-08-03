from timeit_helper import profile_func
import random


def create_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    return matrix

def bubble_sort(arr): # Big O(n2)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr): # Big O(nxlogn)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr): # Big O(n)
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def main():
    arr = tuple(range(1, 1000000))
    random_num = random.choice(arr)
    print(f"Random Number: {random_num}")
    func_maps = {
    }
    for func_algo, func_test in func_maps.items():
        profile_func(lambda: func_test(arr, random_num),func_algo, 100)

if __name__ == "__main__":
    main()