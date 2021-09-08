MESSAGE = 'Введите число от 0 до 10: '


while True:
    user_value: int = int(input(f'{MESSAGE}'))
    if 10 > user_value > 0:
        print(user_value ** 2)
        break
    else:
        print(f'Число недопустимо')
        continue

