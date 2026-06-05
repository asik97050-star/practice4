

numbers = [10, 20, 30, 40, 50]
target = 30

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Элемент табылды. Индексі:", i)
        found = True
        break

if not found:
    print("Элемент табылмады")

# Binary Search

numbers = [10, 20, 30, 40, 50, 60, 70]
target = 50

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Binary Search бойынша табылды. Индексі:", mid)
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

# Палиндром тексеру

word = input("Сөз енгізіңіз: ")

if word == word[::-1]:
    print("Бұл палиндром")
else:
    print("Бұл палиндром емес")