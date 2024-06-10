from datetime import datetime

x = int(input("Количество заказов: "))
list = []
for i in range(x):
	d = datetime.now().strftime('%Y-%m-%d')
	n = input("Номер заказа: ")
	p = input("Места: ")
	a = input("Количество: ")
	print("""Boxberry
	NULL
	ПЭК
	Самовывоз
	Деловые линии
	Почта России
	Yandex Market
	Mega Market
	AliExpress
	Образцы
	OZON
	Ярмарка Мастеров
	CDEK
	Wildberries
	DPD
	Бийск""")
	t = input("TK: ")
	print("MP или KF")
	b = input("Branch: ")
	list.append(f"('{d}', {n}, {p}, {a}, '{t}', '{b}'),")
	print("""INSERT INTO
    work (date, number, place, amount, t_c, branch)
VALUES""")
	print(*[item + '\n' for item in list])
	continue
