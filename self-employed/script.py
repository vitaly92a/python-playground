#!/usr/bin/env python3
from os import sys

# Ввод значения для расчёта для суммы налога

#income_wo_tax = float(input("Введите сумму дохода (руб. ₽): "))
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

user_input = input("Введите сумму дохода (руб. ₽): ")

if isfloat(user_input):
    income_wo_tax = float(user_input)
else:
    print("Ошибка") 
    sys.exit()

# Уточняем получателя сформированного чека - юрлицо или физлицо ((i)ndividual or (b)usiness)
client_type = input("\nДля кого формируется чек? \nФизлицо (4) \nЮрлицо (6)\n$$$: ")
if client_type == "4":
    tax_type = 4
elif client_type == "6":
    tax_type = 6
else:
    print("Ошибка") 
    sys.exit()

# Воспроизводим рассёт чека
tax = 0.01 * tax_type * income_wo_tax
income_w_tax = income_wo_tax - tax
print("Налог:", str(tax_type) + "%", "сумма налога:", str(tax), "\nОставшаяся сумма:", str(income_w_tax))
