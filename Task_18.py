"""
18. Ввести з клавіатури числа в стовпчик до тих пір, поки не буде введено число 0. Видалити всі
непарні числа даного списку та вивести його.
Скорий Євген 141
"""

numbers = []
even = []

print("Введіть числа(якщо хочите завершити дію введіть 0)")
while True:
    number = int(input(": "))
    if number == 0:
        break
    else:
        numbers.append(number)
for i in numbers:
    if i % 2 == 0:
        even.append(i)


print("Парні числа - ", even)
