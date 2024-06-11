from func import _kpi_ #Библиотека с функциями KPI
from func import _order_ #Библиотека с функциями заказов
import os
 # Указываем путь к директории
directory = "/workspaces/kupiflakon/files/"
 # Получаем список файлов
files = os.listdir(directory)
 # Выводим список файлов
print('1 - KPI')
print('2 - Orders')
choic = input("Выберите метрику расчета: ")
print(files)
url = input('Введите имя файла csv: ')
start_date = input('Введите начальную дату в формате "год-месяц-день": ')
end_date = input('Введите конечную дату в формате "год-месяц-день": ')

if choic == '1':
    _kpi_(url, start_date, end_date) #Запуск функции KPI
if choic == '2':
    _order_(url, start_date, end_date) #Запуск функции заказов
