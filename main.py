import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('shopping_list.csv')
print(df.head())
df = df[['Name', 'Price', 'Carbon Footprint (g)']]
print(df.head())
df['Carbon Footprint (kg)'] = df['Carbon Footprint (g)'].div(1000)
print(df['Carbon Footprint (kg)'])

df.plot(kind='scatter', x='Price', y='Carbon Footprint (g)', color='red')
df.plot(kind='scatter', x='Price', y='Carbon Footprint (kg)', color='red')
# fig, ax = plt.subplots()
# y = df['Carbon Footprint (g)']
# z = df['Price']
# n = df['Name']
# ax.scatter(z, y)
#
# for i, txt in enumerate(n):
#     ax.annotate(txt, (z[i], y[i]))
#
#
plt.show()
