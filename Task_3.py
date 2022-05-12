"""
3. Дано текст. Замінити всі входження найбільшої цифри її словесним написанням.
Скорий Євген 141
"""

s=str(input("Введіть рядок : "))

numbers =[0]*len(s)

for i in range(len(s)) :
    if s[i].isdigit():
        numbers.append(int(s[i]))

max_numb = max(numbers)
lst = ["нуль", "один", "два", "три", "чотири", "п'ять", "шість" , "сім", "вісім", "дев'ять"]
name = lst[max_numb]
Old = str(max_numb)
New =name
lenOld = len(Old)

while s.find(Old) > 0:
    i = s.find(Old)
    s = s[:i] + New + s[i+lenOld:]
    
print("Рядок після операцій : ", s)