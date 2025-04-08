MIN_AMOUNT = 10
MAX_AMOUNT = 3000

def get_deposit_amount():
    """Отримання та валідація введеної суми"""
    while True:
        try:
            amount = float(input("Введіть суму поповнення (грн): "))
            if amount <= 0:
                print("Сума має бути більше 0 грн!")
                continue
            return amount
        except ValueError:
            print("Будь ласка, введіть числове значення!")

def check_amount(amount):
    """Перевірка суми за допомогою сторожових виразів"""
    if amount < MIN_AMOUNT:
        print(f"Мінімальна сума поповнення – {MIN_AMOUNT} грн!")
        return False
    if amount > MAX_AMOUNT:
        print(f"Максимальна сума поповнення – {MAX_AMOUNT} грн!")
        return False
    return True

def main():
    amount = get_deposit_amount()
    if check_amount(amount):
        print(f"Поповнення на суму {amount:.2f} грн виконано успішно!")

if __name__ == "__main__":
    main()