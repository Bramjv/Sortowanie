from main import random_table,measure_time


def find_min_index(lst, start):
    i = start
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[i]:
            i = j
    return i


def selection_sort(lst):
    for i in range(len(lst)):
        min_index = find_min_index(lst,i)
        lst[i], lst[min_index] = lst[min_index], lst[i]


table = random_table()
print(f"Tablica: {table}")

min_index=find_min_index(table,start=0)

print(f"Indeks minimalnej liczby: {min_index}")
print(f"Minimalna liczba w tablicy: {table[min_index]}")

execution_time = measure_time(selection_sort,table)
print(f"Posortowana tablica: {table}")
print(f"Sortowanie trwało : {execution_time:.6f} sekund")