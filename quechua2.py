# -*- coding: utf-8 -*-

#leemos el excel

import pandas as pd

verbos = pd.read_excel ('quechua.xlsx')

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
