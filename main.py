from google.colab import files
uploaded=files.upload()
print(uploaded)

import pandas as pd
import io

df = pd.read_csv((io.BytesIO(uploaded['C3S_PR_Jan2021_Fig3_DATA_annual_temperatures.csv'])))

x = pd.DataFrame(df)
print(x)

import pandas as pd
import io

# Re-loading df correctly within this cell, assuming 'uploaded' is available from kernel state.
df = pd.read_csv((io.BytesIO(uploaded['C3S_PR_Jan2021_Fig3_DATA_annual_temperatures.csv'])), skiprows=5)

# Strip whitespace from column names to ensure accurate selection
df.columns = df.columns.str.strip()

df_cleaning=df[['ERA5','Year']]
print(df_cleaning.query("ERA5>0.6 and Year<2018"))

import pandas as pd
import io
import seaborn as sns
import matplotlib.pyplot as plt


# Re-loading df correctly within this cell, assuming 'uploaded' is available from kernel state.
df = pd.read_csv((io.BytesIO(uploaded['C3S_PR_Jan2021_Fig3_DATA_annual_temperatures.csv'])), skiprows=5)

# Strip whitespace from column names to ensure accurate selection
df.columns = df.columns.str.strip()

df_cleaning=df[['ERA5','Year']]
print(df_cleaning.plot(x='Year',y='ERA5',kind='line',title='earth temp anomaly',
color='red',))
sns.set_theme(style='darkgrid')
lineplot=sns.lineplot(data=df, x='Year',y='ERA5', marker='o',color='red')

plt.show()
