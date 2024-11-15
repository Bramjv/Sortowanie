from main import random_table,measure_time


def insertion_sort(lst):
    for i in range(len(lst)):
        j = i
        while j > 0 and lst[j-1] > lst[j]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1


table = random_table()
print(f"Tablica: {table}")

execution_time = measure_time(insertion_sort,table)
print(f"Posortowana tablica: {table}")
print(f"Sortowanie trwało : {execution_time:.6f} sekund")