from config import intokf
from config import update
from config import jambs
from config import repeated

print("""
Intokf

Дабавить один или несколько заказов

Update

Обновить количество мест в заказе

Jambs

Ошибка - не то положил
Недовложение - не доложили товар
Лишнее - положили лишнее

Repeated

Повтор - отправить повторно
Обмен - замена на другой товар
Возврат - возврат клиента
""")

print("""
1 - Добавить заказ (Intokf)
2 - Обновить данные (Update)
3 - Косяки (Jambs)
4 - Повторы (Repeated)
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
