import streamlit as st
import pandas as pd

st.set_page_config(page_title="Presupuesto UTH", page_icon="💰")

st.title("Calculadora de Gastos Universitarios (UTH)")
st.write("Descubriendo nuevos hábitos y formas de pensar para cuidar tu bolsillo.")

with st.form("budget_form"):
    st.subheader("Ingrese los gastos de su presupuesto")

    ingreso = st.number_input("Ingreso Mensual", min_value=0, max_value=1000000, value=0)
    gastosfijos = st.number_input("Gastos Fijos", min_value=0, max_value=1000000, value=0)
    comida = st.number_input("Comida", min_value=0, max_value=1000000, value=0)
    taxi = st.number_input("Taxi", min_value=0, max_value=1000000, value=0)

    submit = st.form_submit_button("Calcular Balance")

if submit:
    if ingreso <= 0:
        st.warning("Favor ingresar un ingreso mayor a 0")
    else:
        datos = {
            "Concepto": ["Ingresos", "Gastos Fijos", "Comida", "Taxi"],
            "Valor": [ingreso, gastosfijos, comida, taxi]
        }
        df = pd.DataFrame(datos)
        
        total_gastos = gastosfijos + comida + taxi
        balance_total = ingreso - total_gastos
        porcentaje_ahorro = (balance_total / ingreso) * 100

        st.divider()
        st.subheader("📊 Resumen de Gastos")
        st.dataframe(df, use_container_width=True)

        st.divider()
        st.metric("Balance Final", f"L. {balance_total:,.2f}")

        if balance_total > 0:
            st.success(f"✅ ¡Andas recio estas ahorrando el {porcentaje_ahorro:.1f}% de tus ingresos.")
        elif balance_total == 0:
            st.warning("⚖️ Estas palmado. No tenes deudas, pero no t0enes ni un pesito.")
        else:
            st.error(f"🚨 Ojo! Estás gastando L. {abs(balance_total):,.2f} más de lo que ingresas.")