import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('shopping_list_protein.csv')
print(df.head())
print('\n -------------------------------\n ')
# print(df['Protein per 100g'])
df = df[['Name', 'Price', 'Weight/Volume(ml/g)', 'Protein per 100g',
         'Carbon Footprint (g)']]
print(df.head())
print('\n -------------------------------\n ')
print(df[['Name', 'Weight/Volume(ml/g)']])
df = df.drop([22])  # drops 10kg rice
df = df.drop([19]).reset_index(drop=True)  # drops Variety Pack Biscuits
# print(df['Name'])
df['Carbon Footprint (kg)'] = df['Carbon Footprint (g)'].div(1000)
print(df[['Name', 'Carbon Footprint (kg)']])
print(df[['Name', 'Carbon Footprint (g)']])

df_sorted = df.sort_values(by=['Carbon Footprint (kg)'], ascending=False)

df_sorted = df_sorted[['Name', 'Carbon Footprint (kg)']]
print('\n -------------------------------\n ')
print('sorted dataframe \n', df_sorted.head())

print('\n -------------------------------\n ')
df_sorted_least = df.sort_values(by=['Carbon Footprint (g)'], ascending=True)
df_sorted_least = df_sorted_least[['Name', 'Carbon Footprint (g)']]
print('sorted_least dataframe \n', df_sorted_least.head())
print('\n -------------------------------\n ')
Total = df['Carbon Footprint (g)'].sum()
print('total grams:', Total)
print('total kg:', Total / 1000)

# df.plot(kind='scatter', x='Price', y='Carbon Footprint (g)', color='red')
# df.plot(kind='scatter', x='Weight/Volume(ml/g)', y='Carbon Footprint (kg)', color='red')
df.plot(kind='scatter', x='Protein per 100g', y='Carbon Footprint (kg)', color='red')
df.plot(kind='scatter', x='Weight/Volume(ml/g)', y='Carbon Footprint (g)', color='red')


fig, ax = plt.subplots()
y = df['Carbon Footprint (g)']
z = df['Weight/Volume(ml/g)']
n = df['Name']
ax.scatter(z, y)
ax.set_ylabel('Carbon Footprint (g)')
ax.set_xlabel('Weight/Volume(ml/g)')

for i, txt in enumerate(n):
    ax.annotate(txt, (z[i], y[i]))

#


plt.show()

print('\n -------------------------------\n ')
print('whole \n', df[['Name', 'Carbon Footprint (kg)']])
