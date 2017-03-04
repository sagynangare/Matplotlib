import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

start = datetime.datetime(2011, 11, 29)
end = datetime.datetime(2016, 11, 29)
df = web.DataReader("XOM","yahoo", start, end)
print(df.head())
df['Adj Close'].plot()
plt.show()
