"""
8. Дано рядок, що зображає двійкову запис цілого позитивного числа. Вивести десяткову запис цього
ж числа.
Скорий Євген 141
"""


def decimal(n):
    dec = 0
    b = 1
    temp = n
    while (temp):
        digit = temp % 10
        temp = int(temp / 10)

        dec += digit * b
        b = b * 2
    return dec

num = int(input("Введіть число у двійковій системі - "))
print("Число у десятковій системі - ", decimal(num))

