from func import _kpi_ #Библиотека с функциями KPI
from func import _order_ #Библиотека с функциями заказов
choic = input("Выберите метрику расчета - kpi или orders: ")
url = input('Введите имя файла csv: ')
start_date = input('Введите начальную дату в формате "год-месяц-день": ')
end_date = input('Введите конечную дату в формате "год-месяц-день": ')

if choic == 'kpi':
    _kpi_(url, start_date, end_date) #Запуск функции KPI
if choic == 'orders':
    _order_(url, start_date, end_date) #Запуск функции заказов

