"""
9. Дано рядок, що містить принаймні один символ пробілу. Вивести підстроку, розташовану між
першим і останнім пробілом початкового рядка. Якщо рядок містить тільки один пробіл, то вивести
порожний рядок.
Скорий Євген 141
"""

str = input("Введіть строку - ")
s = str
counts = str.count(" ")

if counts == 1 or counts == 0:
    print(" ")
else:
    first = s.find(" ")
    last = s.rfind(" ")
    sub_str = s[first:last]

    print("Підстрока: ", str, " =", sub_str)