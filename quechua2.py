# -*- coding: utf-8 -*-



#leemos el excel

import pandas as pd

import streamlit as st

ruta_imagen_local = "quechuacolores.jpg"

st.image(ruta_imagen_local, use_column_width=True)

st.title(':rainbow[Conjugador de verbos en quechua]')

st.markdown("\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
            
texto = """
    En esta aplicación podrás ingresar verbos del quechua a chanca y conjugarlos según la persona, el número y el tiempo gramatical. Si necesitas información extra sobre cada uno de estos rasgos gramaticales solo necesitas clickear debajo. ¡A divertirse conjugando!
    """

st.markdown(f'<p style="text-align: justify;">{texto}</p>', unsafe_allow_html=True)

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

imagenes_verbo = {
        "tiyay": "vivir.jpg",
        "mikuy": "comer.jpg",
        "apay": "llevar.jpg",
        "tusuy": "bailar.jpg",
        "rimay": "hablar.jpg",
        "puñuy": "dormir"
        
}

st.header('Verbo', divider='rainbow')
base = st.selectbox(
    "Seleccione un verbo en quechua",quechua)

if base in imagenes_verbo:
   ruta_imagen_verbo = imagenes_verbo[base]
   st.image(ruta_imagen_verbo, use_column_width=True)
    
st.write("**El verbo en español es:**",dict_que_esp[base])

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
Esta distinción solo se va a dar en el caso de que se trate de la primer persona plural "nosotros".
El uso del pronombre de la primera persona inclusiva implica que el hablante está hablando con la persona a la que se dirige y también se incluye a sí mismo en el grupo.
El uso de la primera persona exclusiva indica que el hablante está hablando de un grupo que no incluye a la persona a la que se dirige, es decir, excluye solamente al interlocutor.
"""

# Botón para mostrar u ocultar la información
if st.button("ℹ️ ¿Cuál es la diferencia entre primera persona inclusiva y exclusiva?"):
    st.write(contenido_info)
    
st.write("**Seleccionaste:**", persona)
import streamlit as st

explicaciones_tiempo = {
    "presente simple": "El presente simple indica acciones que ocurren habitualmente en el presente.",
    "presente progresivo": "El presente progresivo indica acciones que están ocurriendo en el momento de hablar.",
    "presente habitual": "El presente habitual indica acciones que ocurren regularmente, pero no necesariamente en el momento presente.",
    "pasado experimentado simple": "El pasado experimentado simple indica acciones pasadas que el hablante experimentó personalmente.",
    "pasado experimentado progresivo": "El pasado experimentado progresivo indica acciones pasadas que estaban ocurriendo en un momento específico del pasado.",
    "pasado experimentado habitual": "El pasado experimentado habitual indica acciones pasadas que ocurrían regularmente en el pasado.",
    "pasado no experimentado simple": "El pasado no experimentado simple indica acciones pasadas que no fueron experimentadas personalmente por el hablante.",
    "pasado no experimentado progres": "El pasado no experimentado progresivo indica acciones pasadas que estaban ocurriendo en un momento específico del pasado, pero no fueron experimentadas personalmente por el hablante.",
    "pasado no experimentado habitua": "El pasado no experimentado habitual indica acciones pasadas que ocurrían regularmente en el pasado, pero no fueron experimentadas personalmente por el hablante."
}

st.header('Tiempo', divider='rainbow')
tiempo = st.selectbox("Seleccione un tiempo:", list(explicaciones_tiempo.keys()))

if tiempo in explicaciones_tiempo:
    if st.button(f"ℹ️ ¿Qué es el tiempo '{tiempo}'?"):
        st.write(explicaciones_tiempo[tiempo])

st.write("**Seleccionaste:**",tiempo)
#para número
import streamlit as st

st.header('Número', divider='rainbow')

numero = st.radio(
    "Seleccione un número",
    ["singular", "plural"],
    captions = ["Una persona", "Dos personas o más"])

st.write("**Seleccionaste:**", numero)
st.write(":rainbow[**El verbo conjugado es:**]", conjugacion2(base,numero,persona,tiempo))

ruta_imagen_local2 = "quechuaimagen.jpg"

st.image(ruta_imagen_local2, use_column_width=True)

st.header ('¿Por qué es importante aprender quechua?')

texto = """
    Aprender quechua en Perú es como desbloquear una puerta encantada que te lleva a explorar la riqueza cultural de este país maravilloso. No solo te permite conectar de manera auténtica con millones de personas y sumergirte en sus relatos y costumbres, sino que también es como descubrir un tesoro lingüístico lleno de sonidos y expresiones únicas.
    """

st.markdown(f'<p style="text-align: justify;">{texto}</p>', unsafe_allow_html=True)