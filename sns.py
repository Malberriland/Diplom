import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def linegraph(df_):
    """Return a line graph."""
    df = pd.read_csv(df_)
    df['Date'] = pd.to_datetime(df['Date'])
    plt.figure(figsize=(13, 7))
    sns.lineplot(data=df, x='Date', y='Close', linewidth=3, color='blue', label='Цена закрытия')
    plt.title('Динамика цены', fontsize=15)
    plt.xlabel('')
    plt.ylabel('Цена, USD', fontsize=12)
    plt.grid()
    plt.show()


def bargraph(df_):
    """Return a bar graph."""
    df = pd.read_csv(df_)
    plt.figure(figsize=(13, 7))
    sns.set_style("whitegrid")
    sns.barplot(x='Date', y='Profit/Losses', data=df, hue='Date', palette='muted')
    plt.title('Объем торговли с течением времени', fontsize=15)
    plt.xlabel('')
    plt.ylabel('Прибыль / Убытки, тыс.', fontsize=12)
    # hue - каждый столбец имеет свой цвет
    plt.show()


def piegraph():
    """Return a pie graph."""
    data = [82, 86, 87, 88, 89, 92, 93, 95]
    keys = ['Правительство', 'Розничная торговля', 'Производство', 'Технологии', 'Образование', 'Здравоохранение',
                'Финансы', 'Услуги']

    sns.set_style("whitegrid")
    colors = sns.color_palette("muted")

    plt.figure(figsize=(10, 6))
    plt.pie(data, labels=keys, colors=colors, autopct='%.1f%%')
    plt.title("Цифровая трансформация компаний", fontsize=15)
    plt.show()


linegraph("ohlc.csv")
bargraph('budget_data.csv')
piegraph()
