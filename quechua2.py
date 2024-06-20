# -*- coding: utf-8 -*-



#leemos el excel

import pandas as pd

import streamlit as st

st.title(':rainbow[Conjugador de verbos en quechua]')

st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
            
st.markdown("""
¡Bienvenido al conjugador de verbos en quechua! En esta aplicación podrás ingresar verbos del quechua a chanca y conjugarlos según la persona, el número y el tiempo gramatical. Si necesitas información extra sobre cada uno de estos rasgos gramaticales solo necesitas clickear debajo ¡A divertirse conjugando!
""")


verbos = pd.read_excel ('quechua.xlsx')

######################################################################
#######################################################################

import pandas as pd

quechua = pd.read_excel('tiempo.xlsx')

quechua = pd.ExcelFile('tiempo.xlsx')

D = {}

for hoja in quechua.sheet_names:

  df = pd.read_excel ('tiempo.xlsx', sheet_name=hoja)
  c = df.columns
  df.set_index(c[0], inplace=True)
  print (f'Hoja:{hoja}')
  print (df.head())

  d = df.to_dict()

  D[hoja] = d


def conj_quechua(base,numero,persona,tiempo):
  return base + D[tiempo][numero][persona]

quechua_pronombres = pd.read_excel('pronombres.xlsx')

pronombres = pd.ExcelFile('pronombres.xlsx')

DP = {}

dfp = pd.read_excel ('pronombres.xlsx')
c = dfp.columns
dfp.set_index(c[0], inplace=True)

dp = dfp.to_dict()

def conjugacion2(base,numero,persona,tiempo):
    
    if numero not in dp:
         st.error(f"Clave '{numero}' no encontrada en el diccionario 'dp'.")
         return
    if persona not in dp[numero]:
         st.error(f"Clave '{persona}' no encontrada en el diccionario anidado dentro de 'dp[{numero}]'.")
         return
    if tiempo not in D:
         st.error(f"Clave '{tiempo}' no encontrada en el diccionario 'D'.")
         return
    if numero not in D[tiempo]:
         st.error(f"Clave '{numero}' no encontrada en el diccionario anidado dentro de 'D[{tiempo}]'.")
         return
    if persona not in D[tiempo][numero]:
         st.error(f"Clave '{persona}' no encontrada en el diccionario anidado dentro de 'D[{tiempo}][{numero}]'.")
         return
    return dp[numero][persona] + ' ' + base + D[tiempo][numero][persona]
    

#######################################################################
#######################################################################

##diccionario

quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua,espanol))

##importamos streamlit


import streamlit as st
import streamlit as st

st.header('Verbo', divider='rainbow')
base = st.selectbox(
    "Seleccione un verbo en quechua",quechua)

    
st.write("El verbo en espanol es:",dict_que_esp[base])

if base.endswith('y'):
    base = base[:-1]

#para persona
import streamlit as st

st.header('Persona', divider='rainbow')
persona = st.selectbox(
    "Seleccione una persona:",
    ["primera inclusiva","primera exclusiva","segunda","tercera"])

# Contenido adicional que quieres mostrar
contenido_info = """
Esta distinción solo se va a dar en el caso de que se trate de la primer persona plural "nosotros"
El uso del pronombre de la primera persona inclusiva implica que el hablante está hablando con la persona a la que se dirige y también se incluye a sí mismo en el grupo. .
El uso de la primera persona exclusiva indica que el hablante está hablando de un grupo que no incluye a la persona a la que se dirige, es decir, excluye a solamente al interlocutor.
"""

# Botón para mostrar u ocultar la información
if st.button("ℹ️ ¿Cuál es la diferencia entre primera persona inclusiva y exclusiva?"):
    st.write(contenido_info)
    
st.write("Seleccionaste:",persona)
import streamlit as st

st.header('Tiempo', divider='rainbow')
tiempo = st.selectbox(
    "Seleccione un tiempo:",
    ["presente simple","presente progresivo", "presente habitual","pasado experimentado simple","pasado experimentado progresivo","pasado experimentado habitual","pasado no experimentado simple", "pasado no experimentado progres","pasado no experimentado habitua"])
st.write("Seleccionaste:",tiempo)
#para número
import streamlit as st

st.header('Número', divider='rainbow')
numero = st.selectbox(
    "Seleccione un número:",
    ["singular","plural"])

st.write("Seleccionaste:", numero)
st.write("El verbo conjugado es:", conjugacion2(base,numero,persona,tiempo))

