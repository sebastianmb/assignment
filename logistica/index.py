tar librerias
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
#Export Dataframe to excel
prueba=pd.DataFrame(merged_inner)
​
filename='prueba.xlsx'
​
prueba.to_excel(filename)
​
​
print('prueba record successfully exported into Excel File')
​
prueba record successfully exported into Excel File
df = prueba.loc[:, ~prueba.columns.str.contains('^Unnamed')]
​
filename='df.xlsx'
​
prueba.to_excel(filename)
​
​
print('prueba record successfully exported into Excel File')
​
prueba record successfully exported into Excel File