import random
import timeit


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

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def generate_data(size):
    return [random.randint(0, size) for _ in range(size)]


data_sizes = [100, 1000, 5000, 10000]

for size in data_sizes:
    test_data = generate_data(size)

    merge_time = timeit.timeit(lambda: merge_sort(test_data.copy()), number=10)
    insertion_time = timeit.timeit(lambda: insertion_sort(test_data.copy()), number=10)
    timsort_time = timeit.timeit(lambda: sorted(test_data.copy()), number=10)

    print(f"Data Size: {size}")
    print(f"Merge Sort Time: {merge_time:.6f}s")
    print(f"Insertion Sort Time: {insertion_time:.6f}s")
    print(f"Timsort Time (sorted): {timsort_time:.6f}s")
    print("=" * 40)

'''
Merge Sort: На малих наборах даних (наприклад, 100 елементів) Merge Sort працює повільніше,
ніж Insertion Sort, через накладні витрати на рекурсію та злиття.
На великих наборах даних (наприклад, 10 000 елементів) Merge Sort значно швидший,
ніж Insertion Sort, але повільніший, ніж Timsort

Insertion Sort: На малих наборах даних (наприклад, 100 елементів) Insertion Sort працює дуже швидко, 
оскільки його складність близька до O(n)на майже відсортованих даних.
На великих наборах даних (наприклад, 10 000 елементів) Insertion Sort стає дуже повільним
через квадратичну складність.

Timsort: Timsort є найшвидшим алгоритмом на всіх наборах даних. 
Він поєднує переваги Merge Sort (ефективність на великих даних) 
та Insertion Sort (ефективність на малих або майже відсортованих даних).
На малих наборах даних Timsort працює майже миттєво, а на великих — значно швидше, ніж Merge Sort і Insertion Sort.


Timsort є оптимальним вибором для більшості практичних завдань. Він поєднує в собі швидкість Insertion Sort
на малих даних та стабільність Merge Sort на великих даних.
'''