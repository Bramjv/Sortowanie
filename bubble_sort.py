from main import random_table,measure_time


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


table = random_table()
print(f"Tablica: {table}")

execution_time = measure_time(bubble_sort,table)
print(f"Posortowana tablica: {table}")
print(f"Sortowanie trwało : {execution_time:.6f} sekund")