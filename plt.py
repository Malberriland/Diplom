import pandas as pd
import matplotlib.pyplot as plt


def linegraph(df_):
    """Return a line graph."""
    df = pd.read_csv(df_)
    df['Date'] = pd.to_datetime(df['Date'])
    # Преобразует значения "Date" в объекты datetime

    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], alpha=0.7, label="Цена закрытия", linewidth=3, color='b')
    plt.title('Динамика цены', fontsize=16)
    plt.ylabel('Цена, USD', fontsize=12)
    plt.legend()
    plt.grid()
    plt.show()


def some_linegraph(df_):
    """Return some line graphs."""
    df = pd.read_csv(df_)
    date = df.set_index('Date')
    # возвращает новый DataFrame с указанным набором столбцов

    date.plot(subplots=True, figsize=(10, 6))
    plt.legend(loc='best')
    plt.suptitle(
        'Цены открытия, максимума, минимума, закрытия, прил. к закрытию',
        fontsize=16
    )
    plt.xlabel('')
    plt.show()


def bargraph(df_):
    """Return a bar graph."""
    df = pd.read_csv(df_)
    plt.figure(figsize=(15, 7))
    plt.bar(df['Date'], df['Profit/Losses'])
    plt.title('Объем торговли с течением времени', fontsize=14)
    plt.xlabel('')
    plt.ylabel('Прибыль / Убытки, тыс.')
    plt.show()


def piegraph():
    """Return a pie graph."""
    # Цвет для круговой диаграммы
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    import numpy as np
    cmap = plt.get_cmap("tab20c")
    other_colors = cmap(np.arange(3)*4)

    data = [82, 86, 87, 88, 89, 92, 93, 95]
    keys = ['Правительство', 'Розничная торговля', 'Производство', 'Технологии', 'Образование', 'Здравоохранение',
            'Финансы', 'Услуги']

    plt.subplots(figsize=[10, 6])
    plt.pie(x=data, labels=keys, wedgeprops=dict(width=0.2), colors=colors)
    plt.title("Цифровая трансформация компаний", fontsize=14)
    plt.show()


linegraph("ohlc.csv")
some_linegraph("ohlc.csv")
bargraph('budget_data.csv')
piegraph()
