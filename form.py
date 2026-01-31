import streamlit as st

st.title("Formulario de Registro Estudiantil IP-2026")

nombre = st.text_input("Nombre Completo")
edad = st.number_input("Edad", min_value=0, max_value=120)
carrera = st.selectbox("Carrera", ["Ingeniería en Computación", "Diseño Web", "Técnico en Informática", "Ingeniería en Electrónica", "Ingeniería en Electrónica", "Ingeniería en Electrónica"])
comentario = st.text_area("Comentarios adicional (opcional)")

if st.button("Enviar"):
    st.write("Datos enviados correctamente:")
    st.write(f"**Nombre completo** :{nombre}")
    st.write(f"**Edad** :{edad}")
    st.write(f"**Carrera seleccionada** :{carrera}")
    st.write(f"**Comentarios** :{comentario}")
    st.success("¡Formlario enviado correctamente!")