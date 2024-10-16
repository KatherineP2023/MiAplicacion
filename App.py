import streamlit as st
import pandas as pd

st.title("Mi Primera Aplicación")
st.sidebar.title("Parámetros")
st.sidebar.image("Test.jpg")

modulo = st.sidebar.selectbox("Seleccione el módulo",["Módulo 1","Módulo 2", "Módulo 3" ])

if modulo == "Módulo 1":
    st.write("Estás en el módulo 1")
    ge = st.number_input("Ingrese la gravedad específica", min_value=0.1, max_value=1.0, value=0.8)
    api = (141.5/ge)-131.5
    st.write("El grado API es:", api)
elif modulo == "Módulo 2":
    st.write("Estás en el módulo 2")
    df = pd.read_excel("Resultado.xlsx")
    st.write(df)
else:
    st.write("Estás en el módulo 3")
    uploadfile = st.file_uploader("Sube tu archivo csv, excel o vol",type=["csv", "xlsx", "vol"])

    if uploadfile is not None:
        if uploadfile.name.endswith(".csv"):
            df = pd.read_csv(uploadfile)
        elif uploadfile.name.endswith(".xlsx"):
            df = pd.read_excel(uploadfile)
        elif uploadfile.name.endswith(".vol"):
            df = uploadfile.read()
        st.write(df)        
    else:
        st.write("Por favor sube un archivo csv o excel")