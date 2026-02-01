import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sistema El Dorado", layout="wide")


if "inventario" not in st.session_state:

    st.session_state.inventario = pd.DataFrame(
        {"Producto": ["Leche", "Pan", "Huevos"], "Precio": [25.0, 15.0, 4.0]}
    )

if "carrito" not in st.session_state:
    st.session_state.carrito = pd.DataFrame(
        columns=["Producto", "Precio", "Cantidad", "Subtotal"]
    )


st.sidebar.header("📦 Gestión de Inventario")
with st.sidebar.form("admin_inventario"):
    nuevo_nombre = st.text_input("Nombre del Nuevo Producto")
    nuevo_precio = st.number_input("Precio de Venta", min_value=0.0, step=0.1)
    btn_inventario = st.form_submit_button("Añadir al Inventario")

if btn_inventario and nuevo_nombre:
    nueva_item = pd.DataFrame({"Producto": [nuevo_nombre], "Precio": [nuevo_precio]})
    st.session_state.inventario = pd.concat([st.session_state.inventario, nueva_item], ignore_index=True)
    st.sidebar.success(f"{nuevo_nombre} registrado.")

st.sidebar.subheader("Productos Disponibles")
st.sidebar.dataframe(st.session_state.inventario, use_container_width=True)


st.title("Supermercado El Dorado")

col_izq, col_der = st.columns([1, 1.5])

with col_izq:
    st.subheader("Punto de Venta")
    with st.form("formulario_venta", clear_on_submit=True):
       
        opciones_productos = st.session_state.inventario["Producto"].tolist()
        producto_sel = st.selectbox("Seleccione Producto", opciones_productos)
        
        cantidad = st.number_input("Cantidad a vender", min_value=1, step=1)
        btn_venta = st.form_submit_button("Agregar al Carrito")

    if btn_venta:
        
        precio_unitario = st.session_state.inventario.loc[
            st.session_state.inventario["Producto"] == producto_sel, "Precio"
        ].values[0]
        
        subtotal = precio_unitario * cantidad
        
        nueva_fila = pd.DataFrame({
            "Producto": [producto_sel],
            "Precio": [precio_unitario],
            "Cantidad": [cantidad],
            "Subtotal": [subtotal]
        })
        
        st.session_state.carrito = pd.concat([st.session_state.carrito, nueva_fila], ignore_index=True)
        st.toast(f"Agregado: {producto_sel}")

with col_der:
    st.subheader("Detalle del Carrito")
    st.dataframe(st.session_state.carrito, use_container_width=True)
    
    if st.button("Vaciar Carrito"):
        st.session_state.carrito = pd.DataFrame(columns=["Producto", "Precio", "Cantidad", "Subtotal"])
        st.rerun()

with st.popover("Notebook del codigo"):
    st.markdown(
        """
Sistema de Mercado El Dorado
Elaborado por Igmar Sanchez
Clase : Computación en La Nube

¿Qué hace st.session_state?
Es la "memoria" de la aplicación. Como Streamlit recarga todo el código por completo
cada vez que presionas un botón, sin st.session_state el inventario y el carrito volverían a su estado
inicial (es decir, vacios). Gracias a esto, los productos que se agregan se mantienen
guardados durante toda la sesión del usuario.

¿Qué hace el proceso de cálculo?
Dentro del formulario de venta, el programa busca el precio del producto seleccionado en el inventario,
lo multiplica por la cantidad ingresada para obtener el Subtotal, y empaqueta esos datos en un nuevo DataFrame (fila)
que se concatena al carrito principal.

¿Por qué se usa st.form()?
Lo usas para agrupar el selector de productos y la cantidad. Esto evita que la aplicación intente actualizarse o dar
errores mientras el usuario todavía está eligiendo qué comprar. Solo cuando se presiona el st.form_submit_button,
los datos se procesan juntos.

¿Qué se muestra con st.dataframe()?
Muestra una tabla interactiva en la interfaz web con el contenido actual de tus DataFrames
(st.session_state.inventario o st.session_state.carrito), permitiendo ver al usuario los productos de forma organizada.
""")

if not st.session_state.carrito.empty:
    st.divider()
    if st.button("GENERAR FACTURA FINAL"):
        subtotal_g = st.session_state.carrito["Subtotal"].sum()
        isv = subtotal_g * 0.15
        total = subtotal_g + isv
        
        c1, c2 = st.columns(2)
        with c1:
            st.write("### Resumen de Cuenta")
            st.write(f"Subtotal:")
            st.write(f"ISV (15%):")
            st.markdown(f"**TOTAL A PAGAR:**")
        with c2:
            st.write("### ---")
            st.write(f"L. {subtotal_g:,.2f}")
            st.write(f"L. {isv:,.2f}")
            st.markdown(f"### L. {total:,.2f}")
        
        st.balloons()
