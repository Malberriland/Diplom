import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ohlc.csv")
# Pandas.to_datetime() — это метод, который используется для преобразования различных типов данных в объекты datetime.
df['Date'] = pd.to_datetime(df['Date'])
# Метод set_index() в Pandas возвращает новый DataFrame с указанным набором столбцов.
date = df.set_index('Date')

# Линейный график
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], alpha=0.7, label="Цена закрытия", linewidth=3, color='b')
plt.title('Динамика цены', fontsize=16)
plt.legend()
plt.grid()
plt.show()


# Несколько линейных графиков
date.plot(subplots=True, figsize=(10, 6))
plt.legend(loc='best')
plt.suptitle(
    'Цены открытия, максимума, минимума, закрытия, прил. к закрытию',
    fontsize=16
)
plt.xlabel('')
plt.show()


# Гистограмма
df = pd.read_csv('budget_data.csv')
plt.figure(figsize=(15, 7))
plt.bar(df['Date'], df['Profit/Losses'])
plt.title('Объем торговли с течением времени', fontsize=14)
plt.xlabel('')
plt.ylabel('Прибыль / Убытки, тыс.')
plt.show()


# Цвет для круговой диаграммы
import numpy as np
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(3)*4)
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Круговая диаграмма
data = [82, 86, 87, 88, 89, 92, 93, 95]
keys = ['Правительство', 'Розничная торговля', 'Производство', 'Технологии', 'Образование', 'Здравоохранение',
        'Финансы', 'Услуги']
pie, ax = plt.subplots(figsize=[10, 6])

plt.pie(x=data, labels=keys, wedgeprops=dict(width=0.2), colors=colors)
plt.title("Цифровая трансформация компаний", fontsize=14)
plt.show()
