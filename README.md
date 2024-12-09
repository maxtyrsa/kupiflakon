<h3>Купи-Флакон</h3>

Этот проект Kupi-Flakon обладает большим потенциалом для оптимизации процессов и повышения операционной эффективности. Анализ количества собранных заказов позволяет определить пиковое рабочее время и более эффективно распределять ресурсы. Расчет коэффициента эффективности сотрудника помогает выявить слабые места в работе персонала и принять меры по их улучшению.

Анализ показателей среднего количества заказов за определенный период времени позволяет выявить тенденции и изменения спроса на товары. Это помогает оптимизировать запасы и более эффективно управлять производственным процессом. Анализ показателей по дням недели также позволяет оптимизировать график работы и распределение задач между сотрудниками, исходя из пиковой нагрузки в определенные дни.

Внедрение автоматизированных систем учета и анализа данных в проекте Kupi-Flakon значительно упрощает процесс принятия управленческих решений и позволяет оперативно реагировать на изменения рыночных условий. Использование современных технологий аналитики помогает повысить эффективность работы интернет-магазина и улучшить качество обслуживания клиентов.

<h3>Информационная панель</h3>

Данные за 2024

Показывает тенденцию изменения количества заказов определенных компаний за период с Марта по Июнь.

![Marketplace_lineplot](https://github.com/maxtyrsa/kupiflakon/blob/main/dashbord/Маркетплейс-12.06.2024,%2023_48_10.png?raw=true)

![Kupiflakon_lineplot](https://github.com/maxtyrsa/kupiflakon/blob/main/dashbord/Купи-Флакон-12.06.2024,%2023_48_49.png?raw=true)

Количество заказов по дням за период с Марта по Июнь. На данном графике видно что в подразделении Маркетплейс найболее загруженый день Понедельник, найменее загружена Среда. Суббота и Воскресенье не включены в расчет т.к сборка заказов в эти дни была единоразовой.
По заказам с Сайта найболее загружена Среда, найменее загружен Понедельник. Суббота и Воскресенье так же не включены в расчет.

![Marketplace_barplot](https://github.com/maxtyrsa/kupiflakon/blob/main/dashbord/День%20MP-12.06.2024,%2023_49_04.png?raw=true) ![Kupiflakon_barplot](https://github.com/maxtyrsa/kupiflakon/blob/main/dashbord/День%20Купи-Флакон-12.06.2024,%2023_49_18.png?raw=true)

Процент количества заказов определенных компаний в подразделении Маркетплейс больше всего заказо у компании Ozon - 80.5%
По заказам с Сайта больше всего заказов у компании CDEK - 54.9%

Маркетплейс

![Marketplace_diagram](https://github.com/maxtyrsa/kupiflakon/blob/main/dashbord/Маркетплейс%20проценты-13.06.2024,%2000_16_50.png?raw=true) 

Купи-Флакон

![Kupiflakon_diagram](https://github.com/maxtyrsa/kupiflakon/blob/main/dashbord/Купи-Флакон%20проценты-13.06.2024,%2000_18_24.png?raw=true)

Коэфициэнт эфективности сотрудника. Расчитываеться медиана от общего количества собраных заказов за данный период с групировкой по дням. Данное значение умнодаеться на количество рабочих дней в месяце и делиться на 3 сегмента (Bad, Good, Super).


Март
                         

![kpi_march](https://github.com/maxtyrsa/kupiflakon/blob/main/dashbord/Март-12.06.2024,%2023_49_50.png?raw=true)


Апрель
                         

![kpi_april](https://github.com/maxtyrsa/kupiflakon/blob/main/dashbord/Апрель-12.06.2024,%2023_50_00.png?raw=true)


Май


![kpi_mai](https://github.com/maxtyrsa/kupiflakon/blob/main/dashbord/Май-12.06.2024,%2023_50_11.png?raw=true)


Июнь


![kpi_juni](https://github.com/maxtyrsa/kupiflakon/blob/main/dashbord/KPI%20Июнь-12.06.2024,%2023_50_26.png?raw=true)

'''
import psycopg2                                       from db_config import get_db_info                     from datetime import datetime                                                                               filename='db_info.ini'                                section='postgres-sample-db'                          db_info = get_db_info(filename,section)                                                                     try:                                                      with psycopg2.connect(**db_info) as db_connection:        print("Успешно подключено к базе данных.")                                                                  with db_connection.cursor() as db_cursor:             # Insert one record                                           x = int(input("Введите количество заказов:" ))                                                              for i in range(x):                                        d = datetime.now().strftime('%Y-%m-%d')                                                                     n = input("Номер заказа: ")                           num = (range(0, 100000))                              numb = num[int(n)]                                    if numb == 0:                                             numb = None                                       p = input("Количество: ")                             print("""                         Выберите ТК:                                          1 - Boxberry                                          2 - ПЭК                                               3 - Самовывоз                                         4 - Деловые линии                                     5 - Почта России                                      6 - Yandex Market                                     7 - Mega Market                                       8 - AliExpress                                        9 - Образцы                                           10 - OZON_FBS                                         11 - Ярмарка Мастеров                                 12 - CDEK                                             13 - WB_FBS                                           14 - DPD                                              15 - Бийск                                            --------------                                        16 - OZON_FBO                                         17 - WB_FBO                                                  """)                                                               t = int(input("TK: "))                                list_tk = [' ',  'Boxberry', 'ПЭК', 'Самовывоз', 'Деловые линии', 'Почта России', 'Yandex Market', 'Mega Market', 'AliExpress', 'Образцы', 'OZON_FBS', 'Ярмарка Мастеров', 'CDEK', 'WB_FBS', 'DPD', 'Бийск', 'OZON_FBO', 'WB_FBO']                                            tk = list_tk[int(t)]                                  print("""                         Выберите подразделение:                               1 - MP                                                2 - KF                                                3 - Pack Stage                                               """)                                                               b = input("Branch: ")                                 company = [' ', 'MP', 'KF', 'Pack Stage']                                                                   branch = company[int(b)]                              insert_record = 'INSERT INTO kupiflakon (date, number, place, t_c, branch) VALUES (%s, %s, %s, %s, %s);'                                                          insert_value = (d, numb, p, tk, branch)                                                                     db_cursor.execute(insert_record, insert_value)                                          #except OperationalError:                             #    print("Ошибка подключения к базе данных :/")                                                           except (ValueError, NameError, TypeError):                print("Ошибка ввода данных")                                                                            finally:                                                  if db_connection:                                         db_connection.close()                                 print("Соединение с PostgreSQL закрыто.")
'''
