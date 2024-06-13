from datetime import datetime
p = input("Места: ")
a = input("Количество: ")
d = datetime.now().strftime('%Y-%m-%d')
print("""Выберите ТК:
	1 - Boxberry
	2 - ПЭК
	3 - Самовывоз
	4 - Деловые линии
	5 - Почта России
	6 - Yandex Market
	7 - Mega Market
	8 - AliExpress
	9 - Образцы
	10 - OZON
	11 - Ярмарка Мастеров
	12 - CDEK
	13 - Wildberries
	14 - DPD
	15 - Бийск""")
t = int(input("ТК: "))
ones = [' ',  'Boxberry', 'ПЭК', 'Самовывоз', 'Деловые линии', 'Почта России', 'Yandex Market', 'Mega Market', 'AliExpress', 'Образцы', 'OZON', 'Ярмарка Мастеров', 'CDEK', 'Wildberries', 'DPD', 'Бийск']
word = ones[int(t)]
print(f"UPDATE kupiflakon SET place = {p}, amount = {a} WHERE date = '{d}' and t_c = '{word}';")
