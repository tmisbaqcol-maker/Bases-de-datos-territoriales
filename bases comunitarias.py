import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Sistema Territorial de Liderazgo")

# ================= BASE DE DATOS INTEGRADA =================

data = [
    # --- AMB ---
    ["AMB","Ingrid Torres","Barranquilla","Malvinas - Suroccidente","3207225540",""],
    ["AMB","Cesar Hernandez","Barranquilla","Suroriente - Los Laureles","3174874608",""],
    ["AMB","Humberto Martinez","Barranquilla","Puerto C. - Suroreinte","","Sin numero"],
    ["AMB","Mirna Ramos","Barranquilla","Malvinas - Suroccidente","3137077676",""],
    ["AMB","Sergio Marimon","Barranquilla","Puerto C. La Playa","3157097598",""],
    ["AMB","Miguel Castillo","Soledad","Los Robles","3196015779",""],
    ["AMB","Osvaldo Rodriguez","Malambo","Juan 23","","Contacto Cordina Cesar"],
    ["AMB","Norma Baldovino","Barranquilla","La Pradera","3126612526",""],
    ["AMB","Jhan Naranjo","Barranquilla","Los Jobos","3174640176",""],
    ["AMB","Roberto Carlos","Barranquilla","Olivos II","3207728816",""],
    ["AMB","Alexander Henao","Barranquilla","Villa Nueva","3114219896",""],
    ["AMB","Padre Fernando Eliecer","Barranquilla","San Roque","3106332615",""],
    ["AMB","Felipe Ortiz","Barranquilla","El Bosque","3012817076",""],

    # --- MUNICIPALES ---
    ["Municipal","Juan Carlos Corro","Tubará","", "3215797801",""],
    ["Municipal","Librada Meza","Tubará","", "3172856977",""],
    ["Municipal","Rafael Gonzalez","Tubará","", "3002281833",""],
    ["Municipal","Marinella Ortiz","Santa Lucia","", "3216489932",""],
    ["Municipal","Laila Ortiz","Santa Lucia","", "3106481531",""],
    ["Municipal","Adolfo Perez","Santa Lucia","", "3024116148",""],
    ["Municipal","Jose Ospino","Santa Lucia","", "3117006297",""],
    ["Municipal","Jerusalen Jimenez","Santa Lucia","", "3136912556",""],
    ["Municipal","Malvis De la Hoz","Manatí","", "3233378612",""],
    ["Municipal","Doris Escobar","Manatí","", "3002759871",""],
    ["Municipal","Jose Brochero","Manatí","", "3058680503",""],
    ["Municipal","Jaime Daza","Piojó","", "3147834808",""],
    ["Municipal","Tomasa Imitola","Piojó","", "3147540211",""],
    ["Municipal","Hamilton","Piojó","", "3243165867",""],
    ["Municipal","Ana Durante","Usiacurí","", "3046044667",""],
    ["Municipal","Aracelis Jimenez","Usiacurí","", "3104968538",""],
    ["Municipal","Linna Escorcia","Usiacurí","", "3001984631",""],
    ["Municipal","Martha Roa","Baranoa","", "3207032655",""],
    ["Municipal","Michell Chico","Baranoa","", "3183764056",""],
    ["Municipal","Eliecer Herazo","Polonuevo","", "3135383929",""],
    ["Municipal","Luis Sierra","Luruaco","", "3145311578",""],
    ["Municipal","Hilda Beltran","Luruaco","", "3164380672",""]
]

df = pd.DataFrame(data, columns=["Tipo","Nombre","Territorio","Zona","Telefono","Observacion"])

# ================= TABS =================

tab1, tab2 = st.tabs(["Líderes AMB","Líderes Municipales"])

# ================= AMB =================

with tab1:
    st.header("Coordinación AMB")

    amb = df[df["Tipo"]=="AMB"]

    busqueda = st.text_input("Buscar líder AMB")

    if busqueda:
        amb = amb[amb["Nombre"].str.contains(busqueda, case=False)]

    c1,c2,c3 = st.columns(3)

    c1.metric("Total líderes", len(amb))
    c2.metric("Con teléfono", amb["Telefono"].astype(bool).sum())
    c3.metric("Sin contacto", (amb["Telefono"]=="").sum())

    st.dataframe(amb, use_container_width=True)


# ================= MUNICIPALES =================

with tab2:
    st.header("Coordinación Municipal")

    mun = df[df["Tipo"]=="Municipal"]

    busqueda2 = st.text_input("Buscar líder municipal")

    if busqueda2:
        mun = mun[mun["Nombre"].str.contains(busqueda2, case=False)]

    c1,c2,c3 = st.columns(3)

    c1.metric("Total líderes", len(mun))
    c2.metric("Municipios cubiertos", mun["Territorio"].nunique())
    c3.metric("Registros", len(mun))

    st.dataframe(mun, use_container_width=True)

