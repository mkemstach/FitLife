WATER_PER_KG = 30
ML_TO_L = 1000

print('Привет! Давай начнем.')
name = input('Как тебя зовут?')
print(f'Приятно познакомиться, {name}!')
age = int(input('Сколько вам лет?'))
print('Мне нужны данные для расчета твоего индекса массы тела(ИМТ).')

weight_str = input('Какой твой вес? Введи значение в килограммах:')
height_str = input('Какой твой рост? Введи значение в метрах:')

weight = float(weight_str)
height_cm = float(height_str)

# Формула ИМТ: вес (кг) / (рост (м) в квадрате)
bmi = weight / (height_cm ** 2)


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


water_ml = weight * WATER_PER_KG
water_l = water_ml / ML_TO_L

print(f'Отчет для пользователя: {name}, {age} лет.')
print(f'Твой Индекс Массы Тела: {bmi:.1f}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день')
print('Расчет окончен. Будьте здоровы!')
