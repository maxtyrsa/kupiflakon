from datetime import datetime
x = int(input())
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