n = int(input("Введіть кількість елементів у масиві: "))
array = []
print("Введіть елементи масиву:")
for i in range(n):
    element = float(input(f"Елемент {i + 1}: "))
    array.append(element)
negative_elements = [x for x in array if x < 0]
if negative_elements:
    average_negative = sum(negative_elements) / len(negative_elements)
    print("Середнє арифметичне від'ємних елементів:", average_negative)
else:
    print("У масиві немає від'ємних елементів.")
    #завдання 2
n = 7
array = [[0] * n for _ in range(n)] 
for i in range(n):
    for j in range(i, n):
        array[i][j] = j - i + 1
for row in array:
    print(" ".join(map(str, row)))
