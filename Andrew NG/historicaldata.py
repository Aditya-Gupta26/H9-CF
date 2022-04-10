import pandas as pd
from Historic_Crypto import HistoricalData
btc_historicals = HistoricalData('BTC-USD',21600,'2017-04-02-00-00','2022-04-02-00-00').retrieve_data()
df = pd.DataFrame(btc_historicals)
df.to_csv('historicaldata.csv')