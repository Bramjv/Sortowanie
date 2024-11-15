from main import random_table,measure_time


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left,right)


def merge(left,right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


table = random_table()
print(f"Tablica: {table}")

execution_time = measure_time(merge_sort,table)
print(f"Posortowana tablica: {table}")
print(f"Sortowanie trwało : {execution_time:.6f} sekund")