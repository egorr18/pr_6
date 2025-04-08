try:
    temperature = float(input("Введіть температуру приміщення (°C): "))
    
    if temperature < 16:
        print("Температура занизька! Увімкніть обігрівач.")
    elif temperature > 28:
        print("Температура зависока! Увімкніть кондиціонер.")
    else:
        if 20 <= temperature <= 24:
            print("Температура ідеальна для роботи!")
        else:
            print("Температура комфортна.")
            
except ValueError:
    print("Помилка: введіть числове значення температури!")