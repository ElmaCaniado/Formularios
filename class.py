import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Sistema de Registro de Clases", layout="wide")

if 'clases' not in st.session_state:
    st.session_state.clases = pd.DataFrame(
        columns=[
            "Nombre de la Clase", 
            "Hora Inicial", 
            "Hora Final", 
            "Fecha de registro", 
            "Aula", 
            "Cupos Disponibles"
        ]
    )
if 'cupos' not in st.session_state:
    st.session_state.cupos = pd.DataFrame(
        columns=[
            "Nombre", 
            "Fecha de registro", 
            "Hora de registro", 
            "Cupos disponibles"
        ]
    )

st.sidebar.header("📝 Gestión de Cupos")
with st.sidebar.form("admin_cupos"):
    if not st.session_state.cupos.empty:
        ultimo_registro = st.session_state.cupos.iloc[-1]
        val_nombre = ultimo_registro["Nombre"]
        val_fecha = ultimo_registro["Fecha de registro"]
        val_hora = ultimo_registro["Hora de registro"]
        val_cupos = ultimo_registro["Cupos disponibles"]
    else:
        val_nombre = ""
        val_fecha = datetime.today()
        val_hora = datetime.now().time()
        val_cupos = "0"

    nuevo_nombre = st.text_input("Nombre de la clase", value=val_nombre)
    nuevo_fecha = st.date_input("Fecha de Registro", value=val_fecha)
    nuevo_hora = st.time_input("Hora de Inicio", value=val_hora)
    nuevo_hora_fin = st.time_input("Hora de Fin", value=val_hora)
    nuevo_cupos = st.text_input("Cupos Disponibles", value=val_cupos)
    btn_cupos = st.form_submit_button("Añadir Clase")
    
if btn_cupos and nuevo_nombre:
    nueva_item = pd.DataFrame({"Nombre": [nuevo_nombre], "Fecha de registro": [nuevo_fecha], "Hora de registro": [nuevo_hora], "Cupos disponibles": [nuevo_cupos]})
    st.session_state.cupos = pd.concat([st.session_state.cupos, nueva_item], ignore_index=True)
    st.sidebar.success(f"{nuevo_nombre} registrado.")

st.sidebar.subheader("Clases Disponibles")


st.title("Registro de Clases")

col_izq, col_der = st.columns([1, 1.5])

with col_izq:
    st.subheader("Registro de Clases")
    with st.form("formulario_clases", clear_on_submit=True):
        
        opciones_cupos = st.session_state.cupos["Nombre"].tolist()
        cupo_sel = st.selectbox("Seleccione Cupo", opciones_cupos)
        
        fecha = st.date_input("Fecha de Registro", value=datetime.today())
        hora_inicio_val = st.time_input("Hora de Inicio", value=datetime.now().time())
        hora_fin_val = st.time_input("Hora de Fin", value=datetime.now().time())
        
        cantidad = st.number_input("Cupos Disponibles", min_value=1, step=1)
        btn_registro = st.form_submit_button("Registrar Clase")


    if btn_registro:
        nueva_item = pd.DataFrame({
            "Nombre de la Clase": [cupo_sel], 
            "Hora Inicial": [hora_inicio_val],
            "Hora Final": [hora_fin_val],     
            "Fecha de registro": [fecha], 
            "Aula": ["Aula 1"], 
            "Cupos Disponibles": [cantidad]
        })
        st.session_state.clases = pd.concat([st.session_state.clases, nueva_item], ignore_index=True)
        st.toast(f"Clase registrada: {cupo_sel}")
        st.rerun()

with col_der:
    st.subheader("Detalle de Clases")
    st.dataframe(st.session_state.clases, use_container_width=True)
    
    if st.button("Vaciar Clases"):
        st.session_state.clases = pd.DataFrame(columns=["Nombre de la Clase", "Hora Inicial", "Hora Final", "Fecha de registro", "Aula", "Cupos Disponibles"])
        st.rerun()
                
        st.balloons()  
    
