WATER_PER_KG = 30
ML_TO_L = 1000


def classify_bmi(bmi):
    """Возвращает категорию ИМТ по заданному значению индекса."""
    if bmi < 18.50:
        return 'дефицит массы тела'
    elif bmi < 25.0:
        return 'нормальная масса тела'
    elif bmi < 30.0:
        return 'избыточная масса тела'
    else:
        return 'ожирение'


print('Привет! Давай начнем.')


while True:
    name = input('Как тебя зовут?').strip()

    if name:
        break

    print('Имя не может быть пустым. Попробуй ещё раз.')


print(f'Приятно познакомиться, {name}!')


while True:
    age_str = input('Сколько Вам лет? ').strip()

    if not age_str:
        print('Поле не может быть пустым. Попробуй ещё раз.')
        continue

    try:
        age = int(age_str)
    except ValueError:
        print('Ошибка: нужно ввести число(например, 25), а не текст.')
        continue

    if age < 1 or age > 120:
        print('Кажется, тут ошибка. Возраст должен быть от 1 до 120 лет.')
        continue

    print(f'Принято! Вам {age} лет.')
    break


print('Мне нужны данные для расчета твоего индекса массы тела(ИМТ).')


while True:
    prompt_weight = ('Введите вес в киллограммах:')
    weight_str = input(prompt_weight).strip()
    if not weight_str:
        print('Поле не может быть пустым. Попробуй ещё раз.')
        continue

    try:
        weight = float(weight_str)
    except ValueError:
        print('Ошибка: нужно ввести число(например, 75.5), а не текст.')
        continue

    if weight < 1 or weight > 635:
        print('Ошибка: вес выглядит нереалистично. Попробуй ещё раз.')
        continue

    print(f'Принято! Ваш вес {weight} килограмм.')
    break


while True:
    prompt_height = ('Введите рост в метрах ')
    height_str = input(prompt_height).strip()
    if not height_str:
        print('Поле не может быть пустым. Попробуй ещё раз.')
        continue

    try:
        height = float(height_str)
    except ValueError:
        print('Ошибка: нужно ввести число(например, 1.75), а не текст.')
        continue

    if height < 0.50 or height > 3.00:
        print('Ошибка: рост выглядит нереалистично. Попробуй ещё раз.')
        continue

    print(f'Принято! Ваш рост {height} метров.')
    break


# Формула ИМТ: вес (кг) / (рост (м) в квадрате)
bmi = weight / (height ** 2)

water_ml = weight * WATER_PER_KG
water_l = water_ml / ML_TO_L

print(f'Отчет для пользователя: {name}, {age} лет.')
print(f'Твой Индекс Массы Тела: {bmi:.1f}')
# print(f'Классификация массы тела: {classify_bmi(bmi)}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день')
print('Расчет окончен. Будьте здоровы!')
