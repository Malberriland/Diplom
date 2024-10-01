import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# Линейный график
df = pd.read_csv('ohlc.csv')
df['Date'] = pd.to_datetime(df['Date'])
date = df.set_index('Date')

plt.figure(figsize=(13, 7))
sns.lineplot(data=df, x='Date', y='Close', linewidth=3)
plt.title('Динамика цены', fontsize=14)
plt.xlabel('')
plt.ylabel('Цена закрытия', fontsize=12)
plt.grid()
plt.show()


# Гистограмма
df = pd.read_csv('budget_data.csv')

plt.figure(figsize=(13, 7))
sns.set_style("whitegrid")
sns.barplot(x='Date', y='Profit/Losses', data=df, hue='Date', palette='viridis')
plt.title('Объем торговли с течением времени', fontsize=14)
plt.xlabel('')
plt.ylabel('Прибыль / Убытки, тыс.')
# hue - каждый столбец имеет свой цвет
plt.show()


# Круговая диаграмма
data = [82, 86, 87, 88, 89, 92, 93, 95]
keys = ['Правительство', 'Розничная торговля', 'Производство', 'Технологии', 'Образование', 'Здравоохранение',
        'Финансы', 'Услуги']

sns.set_style("whitegrid")
colors = sns.color_palette("pastel")

plt.figure(figsize=(10, 6))
plt.pie(data, labels=keys, colors=colors, autopct='%.1f%%')
plt.title("Цифровая трансформация компаний", fontsize=14)
plt.show()
