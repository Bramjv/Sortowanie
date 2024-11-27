from main import random_table,measure_time


def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[-1]
    lesser = [x for x in lst if x < pivot]
    equal = [x for x in lst if x == pivot]
    greater = [x for x in lst if x > pivot]

    print(f"Pivot: {pivot}")
    print(f"Mniejsze: {lesser}, Równe: {equal}, Większe: {greater}")

    return quick_sort(lesser) + equal + quick_sort(greater)


table = random_table()
print(f"Tablica: {table}")

sorted_table = quick_sort(table)
execution_time = measure_time(quick_sort,table)
print(f"Posortowana tablica: {sorted_table}")
print(f"Sortowanie trwało : {execution_time:.6f} sekund")