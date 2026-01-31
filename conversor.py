import streamlit as st

st.title("Conversor de lempiras a dolares")
lempiras = st.number_input("Ingrese el valor en lempiras", min_value=0.0)
if st.button("Convertir"):
    dolares = lempiras/26.00
    st.write(f"El equivalente en dolares es : ${dolares:.2f}")