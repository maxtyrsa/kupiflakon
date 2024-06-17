from config import intokf
from config import update
from config import jambs
from config import repeated

print("""
1 - Добавить заказ(ы)
2 - Обновить данные
3 - Косяки (jambs)
4 - Повторы (repeated)
	""")
s = int(input("Выбор: "))

if s == 1:
    intokf()
elif s == 2:
    update()
elif s == 3:
    jambs()
elif s == 4:
    repeated()
