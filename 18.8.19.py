amount = 0
tickets = int(input("Введите количество билетов:"))
for age in range(tickets):
    age = int(input("Введите возраст посетителя:"))
    if age < 18:
        amount = amount + 0
    elif age >= 18 and age <= 25:
        amount = amount + 990
    else:
        amount = amount + 1390
if amount == 0:
    print("Для вас вход бесплатный!")
else:
    print("Количество билетов:", tickets, "шт." )
if tickets >= 4 :
    discount = amount * 0.1
    print("К оплате, с учетом скидки:", (int(amount - discount)), "руб.")
if tickets <= 3 :
    nodiscount = amount
    print("К оплате:", nodiscount, "руб.")