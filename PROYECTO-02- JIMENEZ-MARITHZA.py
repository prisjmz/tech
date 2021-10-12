
import pandas as pd
pd.plotting.register_matplotlib_converters()
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns


datos = pd.read_csv("synergy_logistics_database.csv")
datos_df = pd.DataFrame(datos)

print(datos.head())
datos.set_index('register_id', inplace=True)
print(datos.loc[datos['direction']== 'Exports',['origin','destination']])

print('las rutas con más exportaciones')
rutas = datos_df.groupby(['direction'])[['origin','destination']].sum()
print(rutas)

plt.figure(figsize=(16,6))
sns.catplot(x='direction', data=datos,kind='count')
plt.show()


plt.figure(figsize=(16,6))
sns.catplot(y='transport_mode', data=datos,kind='count')
plt.show()

plt.figure(figsize=(16,6))
sns.catplot(y='destination', data=datos,kind='count')
plt.show()

plt.figure(figsize=(16,6))
sns.catplot(y='destination', data=datos,kind='count')
plt.show()


#exportaciones= datos_df.loc[datos_df['Exports']=='origin', 'destination'].value_counts() 
#plt.figure(figsize=(16,6))
#sns.catplot(y= 'direction', exportaciones)
#plt.show()
#importaciones = datos_df.loc[datos_df['destination']=='', 'violation'].value_counts().hvplot.barh(alpha=0.3)

#women * men