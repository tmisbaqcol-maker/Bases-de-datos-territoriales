import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Centro de Control Territorial")

df = pd.read_csv("database.csv")

# ---------------- TABS
tab1, tab2 = st.tabs(["Líderes AMB","Líderes Municipales"])

# =========================
# TAB AMB
# =========================

with tab1:

    st.header("Coordinación AMB")

    amb = df[df["Tipo"]=="AMB"]

    busqueda = st.text_input("Buscar líder AMB")

    if busqueda:
        amb = amb[amb["Nombre"].str.contains(busqueda, case=False)]

    col1,col2,col3 = st.columns(3)
    col1.metric("Total", len(amb))
    col2.metric("Alta prioridad", len(amb[amb["Prioridad"]=="Alta"]))
    col3.metric("Alertas", len(amb[amb["Estado"].isin(["Alerta","Inactivo"])]))

    st.data_editor(amb, use_container_width=True, num_rows="dynamic")


# =========================
# TAB MUNICIPALES
# =========================

with tab2:

    st.header("Coordinación Municipal")

    mun = df[df["Tipo"]=="Municipal"]

    busqueda2 = st.text_input("Buscar líder Municipal")

    if busqueda2:
        mun = mun[mun["Nombre"].str.contains(busqueda2, case=False)]

    col1,col2,col3 = st.columns(3)
    col1.metric("Total", len(mun))
    col2.metric("Alta prioridad", len(mun[mun["Prioridad"]=="Alta"]))
    col3.metric("Alertas", len(mun[mun["Estado"].isin(["Alerta","Inactivo"])]))

    st.data_editor(mun, use_container_width=True, num_rows="dynamic")

csv,
"base_territorial.csv",
"texto/csv"
)
