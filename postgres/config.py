def intokf():
    from datetime import datetime
    x = int(input("Количество заказов: "))
    list = []
    for i in range(x):
	    d = datetime.now().strftime('%Y-%m-%d')
	    n = input("Номер заказа: ")
	    num = (range(0, 100000))
	    numb = num[int(n)]
	    if numb == 0:
		    numb = 'NULL'
	    p = input("Количество: ")
	    print("""
Выберите ТК:
1 - Boxberry
2 - ПЭК
3 - Самовывоз
4 - Деловые линии
5 - Почта России
6 - Yandex Market
7 - Mega Market
8 - AliExpress
9 - Образцы
10 - OZON_FBS
11 - Ярмарка Мастеров
12 - CDEK
13 - WB_FBS
14 - DPD
15 - Бийск
--------------
16 - OZON_FBO
17 - WB_FBO
       """)
	    t = int(input("TK: "))
	    list_tk = [' ',  'Boxberry', 'ПЭК', 'Самовывоз', 'Деловые линии', 'Почта России', 'Yandex Market', 'Mega Market', 'AliExpress', 'Образцы', 'OZON_FBS', 'Ярмарка Мастеров', 'CDEK', 'WB_FBS', 'DPD', 'Бийск', 'OZON_FBO', 'WB_FBO']
	    tk = list_tk[int(t)]
	    print("""
Выберите подразделение:
1 - MP
2 - KF
       """)
	    b = input("Branch: ")
	    company = [' ', 'MP', 'KF']
	    branch = company[int(b)]
	    list.append(f"('{d}', {numb}, {p}, '{tk}', '{branch}'),")
	    print("""INSERT INTO
    kupiflakon (date, number, place, t_c, branch)
VALUES""")
	    print(*[item + '\n' for item in list])
	    continue

def update():
    from datetime import datetime
    p = input("Количество: ")
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
    print(f"UPDATE kupiflakon SET place = {p} WHERE date = '{d}' and t_c = '{word}';")

def jambs():
	from datetime import datetime
	x = int(input("Количество заказов: "))
	list = []
	for i in range(x):
		i = input("Введите id: ")
		p = input("Количество: ")
		d = datetime.now().strftime('%Y-%m-%d')
		print("""Выберите статус:
1 - Ошибка
2 - Недовложение
3 - Лишнее
""")
		j = int(input("Статус: "))
		ones = [' ',  'Ошибка', 'Недовложение', 'Лишнее']
		word = ones[int(j)]
		list.append(f"({i}, '{word}', {p}, '{d}'),")
		print("""INSERT INTO
	    jambs (id, jamb, place, date)
	VALUES""")
		print(*[item + '\n' for item in list])
		continue

def repeated():
	from datetime import datetime
	x = int(input("Количество заказов: "))
	list = []
	for i in range(x):
		i = input("Введите id: ")
		p = input("Количество: ")
		d = datetime.now().strftime('%Y-%m-%d')
		print("""Выберите статус:
1 - Повтор
2 - Обмен
3 - Возврат
	""")
		j = int(input("Статус: "))
		ones = [' ',  'Повтор', 'Обмен', 'Возврат']
		word = ones[int(j)]
		list.append(f"({i}, '{word}', {p}, '{d}'),")
		print("""INSERT INTO
	    repeated (id, repeat, place, date)
	VALUES""")
		print(*[item + '\n' for item in list])
		continue