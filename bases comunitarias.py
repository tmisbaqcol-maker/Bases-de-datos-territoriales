import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Sistema de Gestión Territorial")

# ------------------------
# BASE DE DATOS INICIAL
# ------------------------

data = [
["Juan Carlos Corro","Tubará","3215797801","Activo","Media",""],
["Librada Meza","Tubará","3172856977","Activo","Alta",""],
["Rafael Gonzalez","Tubará","3002281833","Inactivo","Baja",""],
["Marinella Ortiz","Santa Lucia","3216489932","Activo","Alta",""],
["Laila Ortiz","Santa Lucia","3106481531","Activo","Media",""],
["Malvis De la Hoz","Manatí","3233378612","Activo","Alta",""],
["Luis Sierra","Luruaco","3145311578","Activo","Alta","Líder fuerte"],
["Eliecer Herazo","Polonuevo","3135383929","Activo","Media",""],
["Martha Roa","Baranoa","3207032655","Activo","Media",""],
["Ingrid Torres","Malvinas","3207225540","Activo","Alta",""],
["Roberto Carlos","Olivos II","3207728816","Activo","Media",""]
]

df = pd.DataFrame(data, columns=[
"Nombre","Territorio","Telefono","Estado","Prioridad","Observaciones"
])

# ------------------------
# SIDEBAR FILTROS
# ------------------------

st.sidebar.header("Filtros")

territorio = st.sidebar.selectbox(
"Territorio",
["Todos"] + sorted(df["Territorio"].unique())
)

estado = st.sidebar.selectbox(
"Estado",
["Todos"] + sorted(df["Estado"].unique())
)

prioridad = st.sidebar.selectbox(
"Prioridad",
["Todos"] + sorted(df["Prioridad"].unique())
)

busqueda = st.sidebar.text_input("Buscar nombre")

# ------------------------
# FILTRADO
# ------------------------

filtered = df.copy()

if territorio != "Todos":
    filtered = filtered[filtered["Territorio"] == territorio]

if estado != "Todos":
    filtered = filtered[filtered["Estado"] == estado]

if prioridad != "Todos":
    filtered = filtered[filtered["Prioridad"] == prioridad]

if busqueda:
    filtered = filtered[filtered["Nombre"].str.contains(busqueda, case=False)]

# ------------------------
# PANEL MÉTRICAS
# ------------------------

col1,col2,col3 = st.columns(3)

col1.metric("Total contactos", len(filtered))
col2.metric("Activos", len(filtered[filtered["Estado"]=="Activo"]))
col3.metric("Alta prioridad", len(filtered[filtered["Prioridad"]=="Alta"]))

st.divider()

# ------------------------
# TABLA EDITABLE
# ------------------------

st.subheader("Base Territorial Editable")

edited = st.data_editor(
filtered,
use_container_width=True,
num_rows="dynamic"
)

# ------------------------
# ALERTAS
# ------------------------

st.subheader("Alertas Territoriales")

alertas = edited[
(edited["Estado"]=="Inactivo") |
(edited["Prioridad"]=="Alta")
]

if len(alertas) > 0:
    st.warning("Territorios que requieren atención")
    st.dataframe(alertas, use_container_width=True)
else:
    st.success("Sin alertas críticas")

# ------------------------
# EXPORTAR
# ------------------------

csv = edited.to_csv(index=False).encode("utf-8")

st.download_button(
"Descargar base filtrada",
csv,
"base_territorial.csv",
"texto/csv"
)
