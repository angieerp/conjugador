# -*- coding: utf-8 -*-

#leemos el excel

import pandas as pd

verbos = pd.read_excel ('quechua.xlsx')

######################################################################
#######################################################################

import pandas as pd

quechua = pd.read_excel('quechua.xlsx')

quechua = pd.ExcelFile('quechua.xlsx')

D = {}

for hoja in quechua.sheet_names:

  df = pd.read_excel ('quechua.xlsx', sheet_name=hoja)
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
  return dp[numero][persona] + ' ' + base + D[tiempo][numero][persona]

#######################################################################
#######################################################################

##diccionario

quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua,espanol))

##importamos streamlit

import streamlit as st

option = st.selectbox(
    "Seleccione un verbo en quechua",quechua)
    
st.write("El verbo en espanol es:",dict_que_esp[option])


#para persona

persona = st.selectbox(
    "Seleccione una persona:",
    ["primera inclusiva","primera exclusiva","segunda","tercera"])
    
st.write("Seleccionaste:",persona)

#para número

numero = st.selectbox(
    "Seleccione un número:",
    ["singular","plural"])

st.write("Seleccionaste:", numero)