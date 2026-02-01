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
