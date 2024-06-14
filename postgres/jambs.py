from datetime import datetime
x = int(input("Количество заказов: ))
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
