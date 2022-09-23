# Importar librerias
import pandas as pd
import numpy as np
import xlrd
#Leer dataframe
path="C:\\ProyectosWeb\\assigment\\logistica\\"
dfcargue= pd.read_excel(path+'cargue.xlsx')
dfassignment=pd.read_excel(path+'asignacion.xlsx')
​
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
print('prueba record successfully exported into Excel File')
​
prueba record successfully exported into Excel File

