import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.now()

df = web.DataReader("XOM", "yahoo", start, end)
print(df)

df["Adj Close"].plot()
plt.show()
