x = int(input("Введите первое число - "))
y = int(input("Введите второе число - "))

thing = input("Выберите действие: +, -, *, /")

match thing:
  case "+":
        result = x + y
        print(f"Результат: {x} + {y} = {result}")
    case "-":
        result = x - y
        print(f"Результат: {x} - {y} = {result}")
