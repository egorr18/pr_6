STOCK_QUANTITY = 20

try:
    order_quantity = int(input("Введіть кількість товару для замовлення: "))
except ValueError:
    print("Помилка: введено нечислове значення!")
    exit()

if order_quantity <= 0:
    print("Помилка: некоректна кількість!")
    exit()

if order_quantity > STOCK_QUANTITY:
    print("На складі недостатньо товару!")
    exit()

print("Ваше замовлення прийнято!")