# -*- coding: utf-8 -*-

#leemos el excel

import pandas as pd

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

base = st.selectbox(
    "Seleccione un verbo en quechua",quechua)

    
st.write("El verbo en espanol es:",dict_que_esp[base])

if base.endswith('y'):
    base = base[:-1]

#para persona

persona = st.selectbox(
    "Seleccione una persona:",
    ["primera inclusiva","primera exclusiva","segunda","tercera"])
    
st.write("Seleccionaste:",persona)

tiempo = st.selectbox(
    "Seleccione un tiempo:",
    ["presente simple","presente progresivo", "presente habitual","pasado experimentado simple","pasado experimentado progresivo","pasado experimentado habitual","pasado no experimentado simple", "pasado no experimentado progres","pasado no experimentado habitua"])

#para número

numero = st.selectbox(
    "Seleccione un número:",
    ["singular","plural"])

st.write("Seleccionaste:", numero)
st.write("El verbo conjugado es:", conjugacion2(base,numero,persona,tiempo))