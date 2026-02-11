import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Tienda de Electrodomesticos", layout="wide")

st.title("Tienda de Electrodomesticos")


produtos = [
    {"Nombre": "Refrigeradora Samsung", "Precio": 15000, "Categoría": "Línea Blanca"},
    {"Nombre": "Lavadora Samsung", "Precio": 12000, "Categoría": "Línea Blanca"},
    {"Nombre": "Microondas Mabe", "Precio": 3500, "Categoría": "Cocina"},
    {"Nombre": "Licuadora", "Precio": 1200, "Categoría": "Cocina"},
    {"Nombre": "Aire Acondicionado Frigidaire 18000 BTU", "Precio": 18000, "Categoría": "Climatización"},
    {"Nombre": "Plancha", "Precio": 800, "Categoría": "Hogar"},
    {"Nombre": "Smart TV 60 pulg Tekno'", "Precio": 14500, "Categoría": "Entretenimiento"},
    {"Nombre": "Estufa", "Precio": 12000, "Categoría": "Cocina"}
]
df_productos = pd.DataFrame(produtos)

st.sidebar.header("Filtros")
precio_max = st.sidebar.slider("Filtrar por precio máximo", 0, 20000, 20000)
df_filtrado = df_productos[df_productos['Precio'] <= precio_max]

st.subheader("Catálogo de Productos Disponibles")
st.table(df_filtrado)

st.subheader("🛒 Selección de Compra")
col1, col2 = st.columns(2)

with col1:
    seleccion = st.selectbox("Seleccione un producto:", df_filtrado['Nombre'])
    precio_unitario = df_productos[df_productos['Nombre'] == seleccion]['Precio'].values[0]

with col2:
    cantidad = st.number_input("Cantidad:", min_value=1, value=1, step=1)

subtotal_producto = precio_unitario * cantidad

st.info(f"Seleccionado: **{seleccion}** | Precio: **L. {precio_unitario:,.2f}** | Subtotal: **L. {subtotal_producto:,.2f}**")

st.write("---")

st.subheader("Datos del Cliente")
c1, c2 = st.columns(2)
with c1:
    nombre_cliente = st.text_input("Nombre Completo")
    rtn_cliente = st.text_input("RTN / Identidad")
with c2:
    fecha_compra = st.date_input("Fecha de Compra", date.today())


if st.button("Generar Factura"):
    if nombre_cliente and rtn_cliente:
        st.success("Factura generada con éxito")

        isv = subtotal_producto * 0.15
        total_pagar = subtotal_producto + isv
        
        st.markdown("RESUMEN DE FACTURACIÓN")
        st.write(f"**Cliente:** {nombre_cliente} | **RTN:** {rtn_cliente}")
        st.write(f"**Fecha:** {fecha_compra}")

        detalle = {
            "Descripción": [seleccion],
            "Cantidad": [cantidad],
            "Precio Unit.": [f"L. {precio_unitario:,.2f}"],
            "Subtotal": [f"L. {subtotal_producto:,.2f}"]
        }
        st.table(pd.DataFrame(detalle))
        

        col_a, col_b = st.columns(2)
        with col_b:
            st.write(f"**Subtotal General:** L. {subtotal_producto:,.2f}")
            st.write(f"**ISV (15%):** L. {isv:,.2f}")
            st.header(f"Total: L. {total_pagar:,.2f}")
    else:
        st.error("Por favor, complete los datos del cliente para facturar.")