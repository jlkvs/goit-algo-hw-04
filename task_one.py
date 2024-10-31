import random
import timeit

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def timsort(arr):
    return sorted(arr)

def measure_time(sort_func, data):
    start_time = timeit.default_timer()
    sort_func(data)
    return timeit.default_timer() - start_time

sizes = [100, 1000, 10000]
results = {"Insertion Sort": [], "Merge Sort": [], "Timsort": []}
for size in sizes:

    random_data = [random.randint(0, size) for _ in range(size)]
    almost_sorted_data = sorted(random_data)
    reverse_sorted_data = sorted(random_data, reverse=True)
    
    results["Insertion Sort"].append(measure_time(insertion_sort, random_data.copy()))
    results["Merge Sort"].append(measure_time(merge_sort, random_data.copy()))
    results["Timsort"].append(measure_time(timsort, random_data.copy()))

    results["Insertion Sort"].append(measure_time(insertion_sort, almost_sorted_data.copy()))
    results["Merge Sort"].append(measure_time(merge_sort, almost_sorted_data.copy()))
    results["Timsort"].append(measure_time(timsort, almost_sorted_data.copy()))

    results["Insertion Sort"].append(measure_time(insertion_sort, reverse_sorted_data.copy()))
    results["Merge Sort"].append(measure_time(merge_sort, reverse_sorted_data.copy()))
    results["Timsort"].append(measure_time(timsort, reverse_sorted_data.copy()))

print(results)
