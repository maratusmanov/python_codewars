#Учитывая массив целых чисел,
#найдите то, которое появляется
#нечетное количество раз.
def find_it(seq):
    unique_array = []
    for i in range(len(seq)):
        if seq[i] not in unique_array:
            unique_array.append(seq[i])

    counts = {}
    for i in range(len(unique_array)):
        counts[unique_array[i]] = seq.count(unique_array[i])

    for key, value in counts.items():
        if value % 2 != 0:
            return key

seq = [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]

print(find_it(seq))


def likes(names):
    num_people = len(names)
    if num_people == 0:
        return "no one likes this"
    elif num_people == 1:
        return f"{names[0]} likes this"
    elif num_people == 2:
        return f"{names[0]} and {names[1]} like this"
    elif num_people == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {num_people - 2} others like this"

names = ['Max', 'John', 'Mark']
print(likes(names))

def duplicate_count(text):
    