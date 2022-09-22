import pandas as pd
import numpy as np
import xlrd

path="C:\\ProyectosWeb\\assigment\\logistica\\"
dfcargue= pd.read_excel(path+'cargue.xlsx')
dfassignment=pd.read_excel(path+'asignacion.xlsx')

print(dfcargue)
#cprint(list(dfcargue))

#dfassignment['check']=dfcargue.Codigo.isin(dfcargue.Codigo)
#print(dfassignment['check'].value_counts())
#print(dfassignment.loc[dfassignment.check== True, 'Codigo'])


#dfassignment['CodigoCargue']=np.where(dfassignment['Codigo']==3,1,0)

