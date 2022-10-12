 Importar librerias
import pandas as pd
import numpy as np
import xlrd
#Leer dataframe
path="C:\\ProyectosWeb\\assigment\\logistica\\"
dfcargue= pd.read_excel(path+'cargue.xlsx')
dfassignment=pd.read_excel(path+'asignacion.xlsx')
​
​
# Get names of indexes for which column Stock has value No
​
# Convertir el campo record_id de integer a float
dfcargue['Codigo'] = dfcargue['Codigo'].astype('int64')
dfcargue['Codigo'].dtype
​
#print(dfcargue)
dtype('int64')
#Merge de los dos dataframes
merged_inner=pd.merge(left=dfcargue, right=dfassignment, left_on='Codigo', right_on='Codigo')
​
#merged_inner
#
#Export Dataframe to excel
prueba=pd.DataFrame(merged_inner)
​
filename='prueba.xlsx'
​
#prueba.to_excel(filename)
​
​
#print('prueba record successfully exported into Excel File')
#prueba
df = prueba.loc[:, ~prueba.columns.str.contains('^Unnamed')]
​
filename='df.xlsx'
​
#prueba.to_excel(filename)
​
​
#print('prueba record successfully exported into Excel File')
#df.head()
#filtrado por niveles
nivel11 = df['Nivel'] == 2.0
nivel11
df_nivel11 = df[nivel11]
#df_nivel11.head()
#filtrado por niveles
nivel2 = df['Nivel'] == 2.0
nivel2
df_nivel2 = pd.DataFrame(df[nivel2])

filename='df_nivel2.xlsx'

df_nivel2.to_excel(filename)

df_nivel2.head()
TotalV2u = df_nivel2['Venta'].sum()

TotalV2p = df_nivel2['Precio'].sum()


print ("Unidades Totales nivel 2: "+TotalV2u.astype(str))
print ("Precio Total nivel 2: "+TotalV2p.astype(str))

#Cantidad de filas y columnas en el filtro nivel 2

index=pd.Series(df_nivel2.shape)

print(index)

personas= input("Ingresa la cantidad de personas que van a cargar en el nivel 2: ")
split=int(index[0]/int(personas))

# Dividir el numero de filas en partes iguales

#Dividir Dataframe en partes iguales ejemplo en dos partes iguales

df_nivel2_1 = df_nivel2.iloc[:split,:]


df_nivel2_2=df_nivel2.iloc[split:,:]


df_nivel2_1.head()
df_nivel2_2.head()

