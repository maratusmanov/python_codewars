#бинарный поиск
def binary_search(list, item):
    #первый элемент
    low = 0
    #последний элемент
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

# Пример использования функции
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 16, 17, 18, 36, 56, 68]

print(binary_search(my_list, 15))  # Вывод: 1 (индекс элемента 3)
#print(binary_search(my_list, -1))  # Вывод: None (элемент -1 не найден)

