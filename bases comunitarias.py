import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(layout="wide")

st.title("Mapa Territorial de Coordinación")

data = [
["Juan Carlos Corro","Tubará",10.8747,-74.9738,"3215797801"],
["Librada Meza","Tubará",10.8747,-74.9738,"3172856977"],
["Rafael Gonzalez","Tubará",10.8747,-74.9738,"3002281833"],
["Luis Sierra","Luruaco",10.6104,-75.1432,"3145311578"],
["Eliecer Herazo","Polonuevo",10.7802,-74.8557,"3135383929"],
["Martha Roa","Baranoa",10.7965,-74.9150,"3207032655"],
["Ingrid Torres","Malvinas",10.9555,-74.8251,"3207225540"],
["Roberto Carlos","Olivos II",10.9685,-74.7813,"3207728816"]
]

df = pd.DataFrame(data, columns=["Nombre","Zona","Lat","Lon","Telefono"])

zona = st.sidebar.selectbox("Zona",["Todas"] + sorted(df["Zona"].unique()))

if zona != "Todas":
    df = df[df["Zona"] == zona]

layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position='[Lon, Lat]',
    get_radius=250,
    pickable=True,
)

view = pdk.ViewState(
    latitude=df["Lat"].mean(),
    longitude=df["Lon"].mean(),
    zoom=9
)

tooltip = {
    "html": "<b>{Nombre}</b><br/>{Zona}<br/>{Telefono}"
}

st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view,
    tooltip=tooltip
))

st.dataframe(df, use_container_width=True)
