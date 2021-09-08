user_first_name = input('Введите Вашу Фамилию: ')
user_second_name = input('Введите Ваше Имя: ')
user_age = int(input('Введите Ваш возраст: '))
user_weight = int(input('Введите Ваш вес: '))


while True:
    if user_age < 30 and (user_weight < 50 or user_weight < 120):
        print('Вы в хорошем состоянии')
        break
    elif 30 < user_age <= 40 and (user_weight < 50 or user_weight > 120):
        print('Вам требуется заняться собой')
        break
    elif user_age > 40 and (user_weight < 50 or user_weight > 120):
        print('Вам требуется врачебный осмотр')
        break
    else:
        print('Вы в хорошем состоянии')
        break


