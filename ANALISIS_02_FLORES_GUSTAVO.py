#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt #Importamos las librerias que se usan, en este caso unicamente, pandas y matplotlib
import pandas as pd


# In[2]:


def ordenamiento(lista):  #hacemos una función que unicamente nos ordena una lista con el metodo bubuja
    longitud=len(lista)-1
    ordenado=False
    while not ordenado: 
        ordenado=True 
        for i in range(0,longitud): 
            if lista[i][1]<lista[i+1][1]: 
                ordenado=False  
                lista[i],lista[i+1]=lista[i+1],lista[i] 
        


# In[3]:


dataframe=pd.read_csv('synergy_logistics_database.csv') #importamos nuestra BD como un dataframe


# In[4]:


dataframe.dtypes  #analizamos que tipo de variables tenemos dentro de cada columna.


# In[5]:


dataframe.info() #analizamos que tan grande es nuestra BD y si existen datos que nos pueden dar porblemas a la hora de tomar estadisitca basica.En este caso nada nos impide trabajar.


# In[6]:


dataframe.head() #vemos como se compone nuestra base se datos con sus primeros 5 datos.


# In[7]:


Exports=dataframe[dataframe['direction'].str.contains('Exports')] #Creamos dos bases de datos diferentes una donde tengamos unicamente exportaciones y una donde unicamente tenga 
Imports=dataframe[dataframe['direction'].str.contains('Imports')] #importaciones


# In[8]:


Exports


# In[9]:


Exports['origin'].value_counts() #En nuestro DF de exportaciones en la columna origin , vemos los diferentes paises de origen 


# In[10]:


ex=Exports['origin'].value_counts() #creamos una variable con esta informacion unicamente para graficar.


# In[233]:


figure=plt.gcf()
plt.figure(figsize=(10,7))
ex.plot.bar()
plt.xlabel('Países')
plt.ylabel('Numero de exportaciones por país.')
plt.title('Exportaciones')
figure.tight_layout()
plt.savefig('num_exportaciones.png',dpi=100,bbox_inches='tight')
plt.show()


# In[12]:


Exp_Ori_China=Exports[Exports['origin'].str.contains('China')] #creamos diferentes DF para los distintos paises de origen
Exp_Ori_Japan=Exports[Exports['origin'].str.contains('Japan')]
Exp_Ori_Netherlands=Exports[Exports['origin'].str.contains('Netherlands')]
Exp_Ori_USA=Exports[Exports['origin'].str.contains('USA')]
Exp_Ori_Germany=Exports[Exports['origin'].str.contains('Germany')]
Exp_Ori_South_Korea=Exports[Exports['origin'].str.contains('South Korea')]
Exp_Ori_Canada=Exports[Exports['origin'].str.contains('Canada')]
Exp_Ori_Mexico=Exports[Exports['origin'].str.contains('Mexico')]
Exp_Ori_Singapore=Exports[Exports['origin'].str.contains('Singapore')]
Exp_Ori_France=Exports[Exports['origin'].str.contains('France')]
Exp_Ori_Australia=Exports[Exports['origin'].str.contains('Australia')]
Exp_Ori_India=Exports[Exports['origin'].str.contains('India')]
Exp_Ori_Brazil=Exports[Exports['origin'].str.contains('Brazil')]
Exp_Ori_Italy=Exports[Exports['origin'].str.contains('Italy')]
Exp_Ori_Spain=Exports[Exports['origin'].str.contains('Spain')]
Exp_Ori_Russia=Exports[Exports['origin'].str.contains('Russia')]
Exp_Ori_Switzerland=Exports[Exports['origin'].str.contains('Switzerland')]
Exp_Ori_Belgium=Exports[Exports['origin'].str.contains('Belgium')]


# In[13]:


Exp_Ori_China


# In[14]:


print(Exp_Ori_China['destination'].value_counts()) # para cada país de origen , checamos sus destinos. En este caso para china 


# In[15]:


china_totales=[] # hacemos un ciclo sobre los paises destino donde sumamos el valor total de cada DF, esto lo apendamos en una lista 
for i in ['Mexico','Spain','Rusia','South Korea','Argentina','Germany','Japan','USA','Belgium','Brazil']:#esto para crear la relacion origen/destino:Ingreso para cada país.
    china_totales.append(['china /'+i,Exp_Ori_China[Exp_Ori_China['destination'].str.contains(i)]['total_value'].sum()])
        


# In[16]:


china_totales


# In[17]:


ordenamiento(china_totales) #ordenamos la lista en orden descendente con nuestra función
china_totales


# In[18]:


print(Exp_Ori_Australia['destination'].value_counts()) #Este mismo proceso se hace para cada país de origen.


# In[19]:


Aus_totales=[]
for i in ['Singapore','Thailand','Philippines','United Kingdom','Brazil','Mexico']:
    Aus_totales.append(['Australia/'+i,Exp_Ori_Australia[Exp_Ori_Australia['destination'].str.contains(i)]['total_value'].sum()])


# In[20]:


ordenamiento(Aus_totales)
Aus_totales


# In[21]:


print(Exp_Ori_Belgium['destination'].value_counts())


# In[22]:


Bel_totales=[]
for i in ['United Kingdom','Netherlands','France','Germany']:
    Bel_totales.append(['Belgica/'+i,Exp_Ori_Belgium[Exp_Ori_Belgium['destination'].str.contains(i)]['total_value'].sum()])


# In[23]:


Bel_totales


# In[24]:


ordenamiento(Bel_totales)
Bel_totales


# In[25]:


Exp_Ori_Brazil['destination'].value_counts()


# In[26]:


BRA_totales=[]
for i in ['Netherlands','Mexico','China','Argentina','USA']:
    BRA_totales.append(['Brazil/'+i,Exp_Ori_Brazil[Exp_Ori_Brazil['destination'].str.contains(i)]['total_value'].sum()])


# In[27]:


BRA_totales


# In[28]:


ordenamiento(BRA_totales)
BRA_totales


# In[29]:


Exp_Ori_Canada['destination'].value_counts()


# In[30]:


Can_totales=[]
for i in ['United Kingdom','Mexico','USA','China','Japan','Brazil']:
    Can_totales.append(['Canada/'+i,Exp_Ori_Canada[Exp_Ori_Canada['destination'].str.contains(i)]['total_value'].sum()])


# In[31]:


Can_totales


# In[32]:


ordenamiento(Can_totales)
Can_totales


# In[33]:


Exp_Ori_France['destination'].value_counts()


# In[34]:


Fra_totales=[]
for i in ['United Kingdom','Netherlands','Germany','Belgium','Spain','USA','Canada','China','Italy','Russia','Austria']:
    Fra_totales.append(['Francia/'+i,Exp_Ori_France[Exp_Ori_France['destination'].str.contains(i)]['total_value'].sum()])


# In[35]:


Fra_totales


# In[36]:


ordenamiento(Fra_totales)
Fra_totales


# In[37]:


Exp_Ori_Germany['destination'].value_counts()


# In[38]:


GER_totales=[]
for i in ['United Kingdom','France','USA','Mexico','South Korea','Italy','China','Canada','Brazil']:
    GER_totales.append(['Germany/'+i,Exp_Ori_Germany[Exp_Ori_Germany['destination'].str.contains(i)]['total_value'].sum()])


# In[39]:


GER_totales


# In[40]:


ordenamiento(GER_totales)
GER_totales


# In[41]:


Exp_Ori_India['destination'].value_counts()


# In[42]:


Ind_totales=[]
for i in ['United Arab Emirates','China','USA','Russia','Japan','Germany']:
    Ind_totales.append(['Inida/'+i,Exp_Ori_India[Exp_Ori_India['destination'].str.contains(i)]['total_value'].sum()])


# In[43]:


Ind_totales


# In[44]:


ordenamiento(Ind_totales)
Ind_totales


# In[45]:


Exp_Ori_Italy['destination'].value_counts()


# In[46]:


Ita_totales=[]
for i in ['United Kingdom','Netherlands','France','Germany','Spain','Switzerland','USA','Croatia','Singapore','Canada','Ireland','Russia']:
    Ita_totales.append(['Italy/'+i,Exp_Ori_Italy[Exp_Ori_Italy['destination'].str.contains(i)]['total_value'].sum()])


# In[47]:


Ita_totales


# In[48]:


ordenamiento(Ita_totales)
Ita_totales


# In[49]:


Exp_Ori_Japan['destination'].value_counts()


# In[50]:


Jap_totales=[]
for i in ['Germany','Brazil','Canada','China','Mexico','USA','Russia','South Korea','Singapore','Switzerland','Spain']:
    Jap_totales.append(['Japan/'+i,Exp_Ori_Japan[Exp_Ori_Japan['destination'].str.contains(i)]['total_value'].sum()])


# In[51]:


Jap_totales


# In[52]:


ordenamiento(Jap_totales)
Jap_totales


# In[53]:


Exp_Ori_Mexico['destination'].value_counts()


# In[54]:


Mex_totales=[]
for i in ['New Zealand','USA','Singapore','Brazil','Japan','Austria','Canada','Peru']:
    Mex_totales.append(['Mexico/'+i,Exp_Ori_Mexico[Exp_Ori_Mexico['destination'].str.contains(i)]['total_value'].sum()])


# In[55]:


Mex_totales


# In[56]:


ordenamiento(Mex_totales)
Mex_totales


# In[57]:


Exp_Ori_Netherlands['destination'].value_counts()


# In[58]:


Neth_totales=[]
for i in ['France','Germany','Belgium','Argentina','Mexico','Brazil']:
    Neth_totales.append(['Netherlands/'+i,Exp_Ori_Netherlands[Exp_Ori_Netherlands['destination'].str.contains(i)]['total_value'].sum()])


# In[59]:


Neth_totales


# In[60]:


ordenamiento(Neth_totales)
Neth_totales


# In[61]:


Exp_Ori_Russia['destination'].value_counts()


# In[62]:


Rus_totales=[]
for i in ['Netherlands','France','Germany','Belorussia','China','Turkey','Japan','India','South Korea']:
    Rus_totales.append(['Rusia/'+i,Exp_Ori_Russia[Exp_Ori_Russia['destination'].str.contains(i)]['total_value'].sum()])


# In[63]:


Rus_totales


# In[64]:


ordenamiento(Rus_totales)
Rus_totales


# In[65]:


Exp_Ori_Singapore['destination'].value_counts()


# In[66]:


Sin_totales=[]
for i in ['USA','Malaysia','Japan','China']:
    Sin_totales.append(['Singapore/'+i,Exp_Ori_Singapore[Exp_Ori_Singapore['destination'].str.contains(i)]['total_value'].sum()])


# In[67]:


Sin_totales


# In[68]:


ordenamiento(Sin_totales)
Sin_totales


# In[69]:


Exp_Ori_South_Korea['destination'].value_counts()


# In[70]:


SK_totales=[]
for i in ['Vietnam','Japan','Mexico','China','Brazil','USA']:
    SK_totales.append(['South Korea/'+i,Exp_Ori_South_Korea[Exp_Ori_South_Korea['destination'].str.contains(i)]['total_value'].sum()])


# In[71]:


SK_totales


# In[72]:


ordenamiento(SK_totales)
SK_totales


# In[73]:


Exp_Ori_Spain['destination'].value_counts()


# In[74]:


SPA_totales=[]
for i in ['France','Germany','Russia','Belgium','Italy','Brazil']:
    SPA_totales.append(['Spain/'+i,Exp_Ori_Spain[Exp_Ori_Spain['destination'].str.contains(i)]['total_value'].sum()])


# In[75]:


SPA_totales


# In[76]:


ordenamiento(SPA_totales)
SPA_totales


# In[77]:


Exp_Ori_Switzerland['destination'].value_counts()


# In[78]:


SWI_totales=[]
for i in ['France','Germany','Russia','Italy']:
    SWI_totales.append(['Switzerland/'+i,Exp_Ori_Switzerland[Exp_Ori_Switzerland['destination'].str.contains(i)]['total_value'].sum()])


# In[79]:


SWI_totales


# In[80]:


ordenamiento(SWI_totales)
SWI_totales


# In[81]:


Exp_Ori_USA['destination'].value_counts()


# In[82]:


USA_totales=[]
for i in ['Netherlands','Belgium','Mexico','United Arab Emirates','Argentina','Canada','Brazil','Singapore','China']:
    USA_totales.append(['USA/'+i,Exp_Ori_USA[Exp_Ori_USA['destination'].str.contains(i)]['total_value'].sum()])


# In[83]:


USA_totales


# In[84]:


ordenamiento(USA_totales)
USA_totales


# ### Vamos a checar las rutas con mas ganancias

# In[85]:


#Ordenamos por los primeros,segundos,terceros,...etc de todos los paises de origen.
primero=[     
Aus_totales[0],
Bel_totales[0],
BRA_totales[0],
Can_totales[0],
china_totales[0],
Fra_totales[0],
GER_totales[0],
Ind_totales[0],
Ita_totales[0],
Jap_totales[0],
Mex_totales[0],
Neth_totales[0],
Rus_totales[0],
Sin_totales[0],
SK_totales[0],
SPA_totales[0],
SWI_totales[0],
USA_totales[0]
]
ordenamiento(primero)


# In[86]:



segundo=[
Aus_totales[1],
Bel_totales[1],
BRA_totales[1],
Can_totales[1],
china_totales[1],
Fra_totales[1],
GER_totales[1],
Ind_totales[1],
Ita_totales[1],
Jap_totales[1],
Mex_totales[1],
Neth_totales[1],
Rus_totales[1],
Sin_totales[1],
SK_totales[1],
SPA_totales[1],
SWI_totales[1],
USA_totales[1]
]
ordenamiento(segundo)


# In[87]:



tercero=[
Aus_totales[2],
Bel_totales[2],
BRA_totales[2],
Can_totales[2],
china_totales[2],
Fra_totales[2],
GER_totales[2],
Ind_totales[2],
Ita_totales[2],
Jap_totales[2],
Mex_totales[2],
Neth_totales[2],
Rus_totales[2],
Sin_totales[2],
SK_totales[2],
SPA_totales[2],
SWI_totales[2],
USA_totales[2]
]
ordenamiento(tercero)


# In[88]:



cuarto=[
Aus_totales[3],
Bel_totales[3],
BRA_totales[3],
Can_totales[3],
china_totales[3],
Fra_totales[3],
GER_totales[3],
Ind_totales[3],
Ita_totales[3],
Jap_totales[3],
Mex_totales[3],
Neth_totales[3],
Rus_totales[3],
Sin_totales[3],
SK_totales[3],
SPA_totales[3],
SWI_totales[3],
USA_totales[3]
]
ordenamiento(cuarto)


# In[89]:



quinto=[
Aus_totales[4],
#Bel_totales[4],
BRA_totales[4],
Can_totales[4],
china_totales[4],
Fra_totales[4],
GER_totales[4],
Ind_totales[4],
Ita_totales[4],
Jap_totales[4],
Mex_totales[4],
Neth_totales[4],
Rus_totales[4],
#Sin_totales[4],
SK_totales[4],
SPA_totales[4],
#SWI_totales[4],
USA_totales[4]
]
ordenamiento(quinto)


# In[90]:


primero


# In[91]:


segundo


# In[92]:


tercero


# In[93]:


cuarto


# In[94]:


quinto


# ### Haciendo una comparación de entradas las diez rutas de exportación con mayores ingresos es:

# In[95]:


#creamos la lista con los 10 valores con mayores ingresos de exportación.
top10_exp=[
    primero[0],
    primero[1],
    primero[2],
    primero[3],
    segundo[0],
    segundo[1],
    primero[4],
    segundo[2],
    primero[5],
    tercero[0]
]


# In[96]:


top10_exp


# In[97]:


ordenamiento(top10_exp)
top10_exp


# In[98]:


exp_top_nombres=[];exp_top_valores=[] #separamos esta lista con sus dos valores para poder graficar.
for i in top10_exp:
    exp_top_nombres.append(i[0])
    exp_top_valores.append(i[1])


# In[234]:


plt.figure(figsize=(10,7))
plt.barh(exp_top_nombres,exp_top_valores,color='lime')
plt.ylabel('Rutas de exportación \n (origen/destino)')
plt.xlabel( 'Total de ingresos por ruta "$"' )
plt.title('Exportaciones')
plt.savefig('top10_exp',dpi=100,bbox_inches='tight')
plt.show()


# # importaciones

# In[100]:


Imports


# In[101]:


Imports['destination'].value_counts() #del mismo modo trabajamos para importaciones, esta vez nuestros paises  estudiar son los de destino 


# In[102]:


im=Imports['destination'].value_counts() #hacemos variable esta DF unicamente para graficar


# In[235]:


plt.figure(figsize=(10,7))
im.plot.bar()
plt.xlabel('Países')
plt.ylabel('Numero de importaciones ´por país')
plt.title('Importaciones')
plt.savefig('num_imp.png',dpi=100,bbox_inches='tight')
plt.show()


# In[104]:


Imp_dest_Thailand=Imports[Imports['destination'].str.contains('Thailand')] #separamos diferentes Df para cada país destino
Imp_dest_China=Imports[Imports['destination'].str.contains('China')]
Imp_dest_Mexico=Imports[Imports['destination'].str.contains('Mexico')]
Imp_dest_Japan=Imports[Imports['destination'].str.contains('Japan')]
Imp_dest_Germany=Imports[Imports['destination'].str.contains('Germany')]
Imp_dest_United_Arab_Emirates=Imports[Imports['destination'].str.contains('United Arab Emirates')]
Imp_dest_Canada=Imports[Imports['destination'].str.contains('Canada')]
Imp_dest_USA=Imports[Imports['destination'].str.contains('USA')]
Imp_dest_Poland=Imports[Imports['destination'].str.contains('Poland')]
Imp_dest_India=Imports[Imports['destination'].str.contains('India')]
Imp_dest_Singapore=Imports[Imports['destination'].str.contains('Singapore')]


# In[105]:


Imp_dest_Canada


# In[106]:


Imp_dest_Canada['origin'].value_counts() #ahora contamos los paises origen para cada pais destino.


# In[107]:


Imp_Can_totales=[] #se procede del mismo modo al ya antes visto en exportaciones.Esto para todos los paises destino.
for i in ['USA','Japan','United Kingdom','Mexico']:
    Imp_Can_totales.append(['destino:Canada/'+i,Imp_dest_Canada[Imp_dest_Canada['origin'].str.contains(i)]['total_value'].sum()])


# In[108]:


Imp_Can_totales


# In[109]:


ordenamiento(Imp_Can_totales)
Imp_Can_totales


# In[110]:


Imp_dest_China['origin'].value_counts()


# In[111]:


Imp_China_totales=[]
for i in ['USA','Mexico','Germany','Brazil']:
    Imp_China_totales.append(['destino:China/'+i,Imp_dest_China[Imp_dest_China['origin'].str.contains(i)]['total_value'].sum()])


# In[112]:


ordenamiento(Imp_China_totales)
Imp_China_totales


# In[113]:


Imp_dest_Germany['origin'].value_counts()


# In[114]:


Imp_Germany_totales=[]
for i in ['USA','Mexico','Spain','France','South Korea','Brazil']:
    Imp_Germany_totales.append(['destino:Germany/'+i,Imp_dest_Germany[Imp_dest_Germany['origin'].str.contains(i)]['total_value'].sum()])


# In[115]:


ordenamiento(Imp_Germany_totales)
Imp_Germany_totales


# In[116]:


Imp_dest_India['origin'].value_counts()


# In[117]:


Imp_India_totales=[]
for i in ['USA','Japan','Russia','Germany','United Arab Emirates']:
    Imp_India_totales.append(['destino:India/'+i,Imp_dest_India[Imp_dest_India['origin'].str.contains(i)]['total_value'].sum()])


# In[118]:


ordenamiento(Imp_India_totales)
Imp_India_totales


# In[119]:


Imp_dest_Japan['origin'].value_counts()


# In[120]:


Imp_Jap_totales=[]
for i in ['USA','Mexico','China','Australia','South Korea']:
    Imp_Jap_totales.append(['destino:Japan/'+i,Imp_dest_Japan[Imp_dest_Japan['origin'].str.contains(i)]['total_value'].sum()])


# In[121]:


ordenamiento(Imp_Jap_totales)
Imp_Jap_totales


# In[122]:


Imp_dest_Mexico['origin'].value_counts()


# In[123]:


Imp_Mex_totales=[]
for i in ['Japan','Germany','South Korea','Spain','Italy','China']:
    Imp_Mex_totales.append(['destino:Mexico/'+i,Imp_dest_Mexico[Imp_dest_Mexico['origin'].str.contains(i)]['total_value'].sum()])


# In[124]:


ordenamiento(Imp_Mex_totales)
Imp_Mex_totales


# In[125]:


Imp_dest_Poland['origin'].value_counts()


# In[126]:


Imp_Poland_totales=[]
for i in ['France','Italy','Germany']:
    Imp_Poland_totales.append(['destino:Poland/'+i,Imp_dest_Poland[Imp_dest_Poland['origin'].str.contains(i)]['total_value'].sum()])


# In[127]:


ordenamiento(Imp_Poland_totales)
Imp_Poland_totales


# In[128]:


Imp_dest_Singapore['origin'].value_counts()


# In[129]:


Imp_singa_totales=[]
for i in ['China','Japan','Malaysia']:
    Imp_singa_totales.append(['destino:Singapore/'+i,Imp_dest_Singapore[Imp_dest_Singapore['origin'].str.contains(i)]['total_value'].sum()])


# In[130]:


ordenamiento(Imp_singa_totales)
Imp_singa_totales


# In[131]:


Imp_dest_Thailand['origin'].value_counts()


# In[132]:


Imp_Thai_totales=[]
for i in ['USA','Japan','Singapore','China','Malaysia']:
    Imp_Thai_totales.append(['destino:Thailand/'+i,Imp_dest_Thailand[Imp_dest_Thailand['origin'].str.contains(i)]['total_value'].sum()])


# In[133]:


ordenamiento(Imp_Thai_totales)
Imp_Thai_totales


# In[134]:


Imp_dest_United_Arab_Emirates['origin'].value_counts()


# In[135]:


Imp_UAE_totales=[]
for i in ['Japan','China','South Korea','Vietnam']:
    Imp_UAE_totales.append(['destino:UAE/'+i,Imp_dest_United_Arab_Emirates[Imp_dest_United_Arab_Emirates['origin'].str.contains(i)]['total_value'].sum()])


# In[136]:


ordenamiento(Imp_UAE_totales)
Imp_UAE_totales


# In[137]:


Imp_dest_USA['origin'].value_counts()


# In[138]:


Imp_USA_totales=[]
for i in ['China','Japan','Canada','Mexico']:
    Imp_USA_totales.append(['destino:USA/'+i,Imp_dest_USA[Imp_dest_USA['origin'].str.contains(i)]['total_value'].sum()])


# In[139]:


ordenamiento(Imp_USA_totales)
Imp_USA_totales


# ### Obtenemos los top 10 en importaciones

# In[141]:


#De manera similar separamos por primeros , segundos, etc de todos los países destino
Imp_primeros=[ 
    Imp_Can_totales[0],
    Imp_China_totales[0],
    Imp_Germany_totales[0],
    Imp_Thai_totales[0],
    Imp_India_totales[0],
    Imp_Poland_totales[0],
    Imp_Mex_totales[0],
    Imp_Jap_totales[0],
    Imp_UAE_totales[0],
    Imp_USA_totales[0],
    Imp_singa_totales[0]
]
ordenamiento(Imp_primeros)


# In[142]:


ordenamiento(Imp_primeros)
Imp_primeros


# In[143]:


Imp_segundos=[
    Imp_Can_totales[1],
    Imp_China_totales[1],
    Imp_Germany_totales[1],
    Imp_Thai_totales[1],
    Imp_India_totales[1],
    Imp_Poland_totales[1],
    Imp_Mex_totales[1],
    Imp_Jap_totales[1],
    Imp_UAE_totales[1],
    Imp_USA_totales[1],
    Imp_singa_totales[1]
]
ordenamiento(Imp_segundos)


# In[144]:


Imp_segundos


# In[145]:


Imp_terceros=[
    Imp_Can_totales[2],
    Imp_China_totales[2],
    Imp_Germany_totales[2],
    Imp_Thai_totales[2],
    Imp_India_totales[2],
    Imp_Poland_totales[2],
    Imp_Mex_totales[2],
    Imp_Jap_totales[2],
    Imp_UAE_totales[2],
    Imp_USA_totales[2],
    Imp_singa_totales[2]
]
ordenamiento(Imp_terceros)


# In[146]:


Imp_terceros


# In[147]:


Imp_cuartos=[
    Imp_Can_totales[3],
    Imp_China_totales[3],
    Imp_Germany_totales[3],
    Imp_Thai_totales[3],
    Imp_India_totales[3],
    #Imp_Poland_totales[3],
    Imp_Mex_totales[3],
    Imp_Jap_totales[3],
    Imp_UAE_totales[3],
    Imp_USA_totales[3],
    #Imp_singa_totales[3]
]
ordenamiento(Imp_cuartos)


# In[148]:


Imp_cuartos


# ### Tomando el top 10 de mayores ventas

# In[149]:


#la lista con el top 10 de importaciones
top10_imp=[
    Imp_primeros[0],
    Imp_primeros[1],
    Imp_segundos[0],
    Imp_terceros[0],
    Imp_primeros[2],
    Imp_primeros[3],
    Imp_primeros[4],
    Imp_segundos[1],
    Imp_primeros[5],
    Imp_segundos[2]
]


# In[150]:


ordenamiento(top10_imp)
top10_imp


# In[151]:


imp_top_nombres=[];imp_top_valores=[] #de igual manera separamos esta lista para poder graficar.
for i in top10_imp:
    imp_top_nombres.append(i[0])
    imp_top_valores.append(i[1])


# In[236]:


#figure=plt.gcf()
plt.figure(figsize=(10,7))
plt.barh(imp_top_nombres,imp_top_valores,color='limegreen',left=0)
plt.ylabel('Rutas de importación \n (destino/origen)')
plt.xlabel( 'Total de ingresos por ruta "$"' )
plt.title('Imprtaciónes')
#figure.tight_layout() 
plt.savefig('top10_imp.png',dpi=100,bbox_inches='tight')
plt.show()


# # Opción 2

# In[153]:


Exports


# In[154]:


exp_caso2=Exports.groupby('transport_mode')['total_value'].sum() #separamos nuestro DF de exportaciones ordenandolo por el medio de transporte y sumamos sus datos de el valor total
#para cada opcion.


# In[237]:


plt.figure(figsize=(10,7))
exp_caso2.plot.bar(color='coral')
plt.ylabel('Total de ingresos para cada medio en exportaciones"$"')
plt.xlabel('Medio de Transporte')
plt.title('Exportaciones')
plt.savefig('ingresos_exp_opc2.png',dpi=100,bbox_inches='tight')


# In[156]:


imp_caso2=Imports.groupby('transport_mode')['total_value'].sum() #Hacemos lo mismo para el DF de importaciones.


# In[238]:


plt.figure(figsize=(10,7))
imp_caso2.plot.bar(color='orangered')
plt.ylabel('Total de ingresos para cada medio en importaciones"$"')
plt.xlabel('Medio de Transporte')
plt.title('Importaciones')
plt.savefig('ingresos_imp_opc2.png',dpi=100,bbox_inches='tight')


# In[158]:


ab=Exports['transport_mode'].value_counts()


# In[159]:


Exports['transport_mode'].value_counts() #aqui unicamente contabilizamos el numero de uso de cada metodo de transporte y se grafico , esto para la Df de exportaciones


# In[198]:


ab.plot.pie(labels=['Sea','Rail','Road','Air'],autopct='%1.1f%%')
plt.xlabel('Exportaciones.')
plt.savefig('pie_exp.png')
plt.show()


# In[161]:


ba=Imports['transport_mode'].value_counts() #se hace lo mismo para la Df de importaciones


# In[162]:


Imports['transport_mode'].value_counts()


# In[200]:


ba.plot.pie(labels=['Sea','Rail','Road','Air'],autopct='%1.1f%%')
plt.xlabel('Importaciones')
plt.savefig('pie_imp.png')
plt.show()


# # Opcion 3

# In[164]:


#Con los DF creados para cada pais de exportaciones , unicamente tomamos la suma de sus valores totales y la dividimos entre la suma de la DF fe exportaciones y le damos un porcentaje 
#Esto es para las exportaciones.
porcentajes=[
(Exp_Ori_China['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Japan['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Netherlands['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_USA['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Germany['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_South_Korea['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Canada['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Mexico['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Singapore['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_France['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Australia['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_India['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Brazil['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Italy['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Spain['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Russia['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Switzerland['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Belgium['total_value'].sum()/Exports['total_value'].sum())*100
]


# In[165]:


#creamos una lista con sus nombres para graficar
nombres=['CHI',
         'JAP',
         'NET',
         'USA',
         'GER',
         'S.K',
         'CAN',
         'MEX',
         'SING',
         'FRA',
         'AUS',
         'IND',
         'BRA',
         'ITA',
         'SPA',
         'RUS',
         'SWI',
         'BEL'
    
]


# In[166]:


porcentajes[0]+porcentajes[3]+porcentajes[9]+porcentajes[5]+porcentajes[15]+porcentajes[1]+porcentajes[4]+porcentajes[6] #Este es la suma de paises que dan el ochenta por ciento


# In[239]:


plt.figure(figsize=(10,7))
plt.bar(nombres,porcentajes,color='silver')
plt.ylabel('% de aportación a la ganancia total de exportaciones.')
plt.xlabel('Países')
plt.title('Exportaciones')
plt.savefig('porcnt_exp_opc3.png',dpi=100,bbox_inches='tight')
plt.show()


# In[168]:


#Hacemos lo mismo para el df de importaciones.
porc_import=[
    (Imp_dest_Thailand['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_China['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_Mexico['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_Japan['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_Germany['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_United_Arab_Emirates['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_Canada['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_USA['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_Poland['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_India['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_Singapore['total_value'].sum()/Imports['total_value'].sum())*100,
]


# In[169]:


nom_import=[
    'ThA',
    'CHI',
    'MEX',
    'JAP',
    'GER',
    'UAE',
    'CAN',
    'USA',
    'POL',
    'IND',
    'SING'
]


# In[170]:


porc_import[0]+porc_import[2]+porc_import[5]+porc_import[3]+porc_import[4]+porc_import[7] #Esta es la suma de los paises que dan ochenta por ciento


# In[240]:


plt.figure(figsize=(10,7))
plt.bar(nom_import,porc_import,color='grey')
plt.ylabel('% de aportación a la ganancia total de importaciones.')
plt.xlabel('Paises')
plt.title('Importaciones')
plt.savefig('prcnt_imp_opc3.png',dpi=100,bbox_inches='tight')
plt.show()


# In[ ]:




