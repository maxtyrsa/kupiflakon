from datetime import datetime

x = int(input("Количество заказов: "))
list = []
for i in range(x):
	d = datetime.now().strftime('%Y-%m-%d')
	print("""NULL - для MP""")
	n = input("Номер заказа: ")
	p = input("Места: ")
	a = input("Количество: ")
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
	t = int(input("TK: "))
	ones = [' ',  'Boxberry', 'ПЭК', 'Самовывоз', 'Деловые линии', 'Почта России', 'Yandex Market', 'Mega Market', 'AliExpress', 'Образцы', 'OZON', 'Ярмарка Мастеров', 'CDEK', 'Wildberries', 'DPD', 'Бийск']
	word = ones[int(t)]
	print("""Выберите подразделение:
	1 - MP
	2 - KF""")
	b = input("Branch: ")
	ones2 = [' ', 'MP', 'KF']
	word1 = ones2[int(b)]
	list.append(f"('{d}', {n}, {p}, {a}, '{word}', '{word1}'),")
	print("""INSERT INTO
    work (date, number, place, amount, t_c, branch)
VALUES""")
	print(*[item + '\n' for item in list])
	continue
