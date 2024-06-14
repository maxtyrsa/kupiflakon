def _kpi_(url, start_date, end_date):
	import pandas as pd
	import numpy as np
	src = url
	df = pd.read_csv('files/'+src+'.csv', sep=';')
	df = df[df['date'].between(start_date, end_date)]
	mp = df.query("branch == 'MP'") \
	.groupby('date', as_index=False) \
	.agg({'place': 'sum'}) \
	.rename(columns={'place': 'counts'})

	kf = df.query("branch == 'KF'") \
	.groupby('date', as_index=False) \
	.agg({'place': 'count'}) \
	.rename(columns={'place': 'counts'})

#Формула расчета KPI: Индекс KPI = ((Факт – База) / (Норма – База)) * 100%. Прежде чем начинать разработку системы KPI, необходимо задать три уровня эффективности: База. Минимальное допустимое значение, которое служит нулевой точкой для отсчета результатов. Норма. Уровень удовлетворительного значения, учитывающий обстоятельства: ситуацию на рынке, сложность работы, возможности конкретного сотрудника. Цель. Уровень выше норматива, к которому следует стремиться.

	mp['kpi'] = round((mp.counts-10)/(103-10)*100, 2)
	mp.sort_values('date', ascending=False)

	kf['kpi'] = round((kf.counts-2)/(26-2)*100, 2)
	kf.sort_values('date', ascending=False)


	def f(row):
	 if row['kpi'] < 25:
			 val = 0
	 elif row['kpi'] < 50:
			 val = 0.1
	 elif row['kpi'] < 75:
			 val = 0.2
	 elif row['kpi'] < 90:
			 val = 0.3
	 elif row['kpi'] < 100:
			 val = 0.4
	 else :
			 val = 0.5
	 return val
	#create new column 'Good' using the function above
	mp['weight'] = mp.apply (f, axis=1)
	mp['result'] = mp.kpi*mp.weight
	mp['money'] = mp.result*55

	kf['weight'] = kf.apply (f, axis=1)
	kf['result'] = kf.kpi*kf.weight
	kf['money'] = kf.result*55

	print ('*'*20, 'KPI Маркетплейс', '*'*20)
	print(mp)
	print('Сумма: ', round((mp.result * 55).sum(), 2))
	print ('*'*20, 'KPI Купи Флакон', '*'*20)
	print(kf)
	print('Сумма: ', round((kf.result * 55).sum(), 2))
	print ('*'*20, 'Итог', '*'*20)
	print('Итого сумма: ', round((mp.result * 55).sum() + (kf.result * 55).sum(), 2))
	print('*'*20, 'Маркетплейс', '*'*20)
	df_mp = df.query(f'branch == "MP"').groupby('t_c', as_index=False)['place'].sum().sort_values('place', ascending=False)
	df_mp['percent'] = df_mp.place/df_mp.place.sum()*100
	print(df_mp)
	print('В среднем за день: ', round(np.median(df_mp.place)), 'шт')
	print('*'*20, 'Купи Флакон', '*'*20)
	df_kf = df.query(f'branch == "KF"').groupby('t_c', as_index=False)['place'].count().sort_values('place', ascending=False)
	df_kf['percent'] = df_kf.place/df_kf.place.sum()*100
	print(df_kf)
	print('В среднем за день: ', round(np.median(df_kf.place)), 'шт')
	print ('*'*20, 'Время сборки', '*'*20)
	time = [4.63, 18.34]
	t1 = round((df_mp.place.sum() * time[0] // 60))
	t2 = round((df_mp.place.sum() * time[0] % 60))
	print(f'Примерное время сборки Маркетплейс: {t1} ч. {t1} мин.')
	t3 = round((df_kf.place.sum() * time[1] // 60))
	t4 = round((df_kf.place.sum() * time[1] % 60))
	print(f'Примерное время сборки Купи Флакон: {t3} ч. {t4} мин.')
	print(f'Итоговое время сборки Купи Флакон и Маркетплейс: {t3+t1} ч. {t4+t2} мин.')

def _order_(url, start_date, end_date):
	import numpy as np
	import pandas as pd
	src = url
	df = pd.read_csv('files/'+src+'.csv', sep=';')
	df = df[df['date'].between(start_date, end_date)]
	mp = df.query("branch == 'MP'")[['date', 'place', 't_c']].reset_index(drop=True).rename(columns={'place': 'counts'}).sort_values('date', ascending=True)

	kf = df.query("branch == 'KF'")[['date', 'number', 't_c']].reset_index(drop=True).sort_values('date', ascending=True)
	kf.number = kf.number.astype(int)
	mp = mp.rename(columns={'date': 'Дата', 'counts': 'Количество', 't_c': 'Компания'})
	kf = kf.rename(columns={'date': 'Дата', 'number': 'Номер заказа', 't_c': 'Компания'})
	print('*'*20, 'Маркетплейс', '*'*20)
	print(mp)
	print('*'*20, 'Купи Флакон', '*'*20)
	print(kf)
	mp.to_csv('mp.csv', index=False)
	kf.to_csv('kf.csv', index=False)
