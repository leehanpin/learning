import pandas as pd

with open("aapl.csv", 'r') as data1:

    gap = pd.read_csv(data1, usecols=('Adj Close', 'Volume'))
    df1 = gap['Adj Close']
    df2 = gap['Volume']
    averageDate = gap['Adj Close'].mean()
    medianDate = df1.median()
    z = (df1 * df2).sum() / df2.sum()
    print(gap)
    print("收盤價最大值：", float(df1.max()))
    print("收盤價最小值：", float(df1.min()))
    print("收盤價平均值：", averageDate)
    print("收盤價中位數：", medianDate)