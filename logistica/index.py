# Importar librerias
import pandas as pd
import numpy as np
import xlrd
import os

#Leer dataframe
path="C:\\ProyectosWeb\\assigment\\logistica\\"
ficheros= os.listdir('C:\\ProyectosWeb\\assigment\\logistica\\rutas')

for fichero in ficheros:
    r=os.path.splitext(fichero)

    dfcargue= pd.read_excel(path+'rutas\\1.xlsx')
    dfassignment=pd.read_excel(path+'asignacion.xlsx')
    print(r) 

#llenar campo nan con 0
dfcargue_fill=dfcargue.fillna(0)

#Eliminar campos con texto
marcas=['COLOMBINA','ALDOR','ALIMENTOS CONCENTRADOS RAZA','AZULK SA','COLOMBIANA DE COMERCIO CORBETA','COMESTIBLES ITALO SA','HARINERA DEL VALLES.A.','HENKEL COLOMBIANA SAS','INDUSTRIAS KATORI','J&J DE COLOMBIA SA','KELLOGG DE COLOMBIA','LABORATORIOS NATURAL FRESHLY','PAPELES NACIONALES SA','PFIZER CONSUMER HEALTCHARE','UNILEVER','VELAS Y VELONES SAN JORGE','INVERSIONES VADISA SOCIEDAD POR ACCIONES SIMPLIFICADA']
dfcargue_ok=dfcargue_fill.replace(marcas,0)

# Convertir el campo record_id de integer a float
dfcargue_ok['Codigo'] = dfcargue_ok['Codigo'].astype('int64')
dfcargue_ok['Codigo'].dtype

#Merge de los dos dataframes
merged_inner=pd.merge(left=dfcargue_ok, right=dfassignment, left_on='Codigo', right_on='Codigo')

#merged_inner
df_ruta = merged_inner.loc[:, ~merged_inner.columns.str.contains('^Unnamed')]

filename='df_ruta.xlsx'

df_ruta.to_excel(filename)


#print('prueba record successfully exported into Excel File')
df_ruta.head()

#filtrado por niveles
ruta=1
Niveles =[1.1,1.2,1.3,2.0,3.0]
filtro = df_ruta['Nivel'] == 1.1

df = pd.DataFrame(columns=['Ruta','Nivel','Unidades', 'Precio'])

for i in Niveles:
    filtro = df_ruta['Nivel'] == i
    filtro
    name= str(i)
    df_nivel = pd.DataFrame(df_ruta[filtro])
    
    totalU = df_nivel['Venta'].sum()
    totalP = df_nivel['Precio'].sum()
    
    df_new_row = pd.DataFrame({ 'Ruta': [ruta], 'Nivel': [name], 'Unidades':[totalU], 'Precio':[totalP] })
      
    df=pd.concat([df, df_new_row])
    if name=='3.0':
        ruta= ruta+1
    
     
    print ("Unidades Totales nivel "+name+": "+totalU.astype(str))
    print ("Precio Total nivel "+name+": "+totalP.astype(str))
    print ("****************************************************************\n")
    
    filename='df_nivel+'+name+'.xlsx'

    df_nivel.to_excel(filename)