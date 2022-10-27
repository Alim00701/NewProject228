z = []


def binary_search(lst, number):
    low = lst[0]
    high = lst[-1]
    mid = len(lst) // 2
    while True:
        if mid < number:
            z.append(mid)
            low = mid
            mid = (low + high) // 2
        elif mid > number:
            z.append(mid)
            high = mid
            mid = (low + mid) // 2
        elif mid == number:
            z.append(mid)
            return "Программа завершена!"


print(binary_search(range(1, 31), 7), f"{z} Кол-во попыток: {len(z)}")


lst_1 = []


def bubble_sort(lst):
    while len(lst) != 0:
        minimum = lst.index(min(lst))
        lst_1.append(lst.pop(minimum))
    return f"Программа отсортировала список: {lst_1}"


print(bubble_sort([53, 27, 81, 16, 4, 96, 69]))
