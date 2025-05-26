import streamlit as st

# Pagina-configuratie
st.set_page_config(page_title="Eetgedrag Vragenlijst", layout="centered")

# Intro en uitleg
st.markdown("### 🌟 Deze vragenlijst is bedoeld voor de ouders van kinderen (2 tot 6 jaar) die moeilijk eten")
st.markdown("<span style='color:darkgreen;font-size:18px;'>Let op: voor een betrouwbaar advies moet u elke vraag zorgvuldig beantwoorden.</span>", unsafe_allow_html=True)

# ✅ Nieuwe, verbeterde CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e6ffe6; /* pastelgroen */
        color: black;
    }

    /* Vraagtekst = zwart */
    label {
        color: black !important;
        font-weight: bold;
    }

    /* Donkergroene container rond de radiobuttons */
    div[data-testid="stRadio"] {
        background-color: #006400;
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 16px;
    }

    /* Radiobutton tekst = wit */
    div[data-testid="stRadio"] label {
        color: white !important;
    }

    /* Verstuurknop donkergroen met witte tekst */
    button[kind="primary"] {
        background-color: #006400;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
    }

    button[kind="primary"]:hover {
        background-color: #228B22;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titel
st.title("Vragenlijst over het eetgedrag van uw kind")



# Vragen en puntensysteem
vragen = [
    ("Heeft uw kind een sterke voorkeur voor bepaalde producten?", [0, 1, 2]),
    ("Weigert uw kind nieuwe producten te proberen?", [0, 1, 2]),
    ("Eet uw kind elke dag dezelfde producten?", [0, 1, 2]),
    ("Eet uw kind minder dan aanbevolen hoeveelheid voor zijn of haar leeftijd?", [0, 1, 2]),
    ("Lijkt uw kind angstig of gestrest rond eetmomenten?", [0, 1, 2]),
    ("Kokhalst uw kind tijdens de maaltijd?", [0, 1, 2]),
    ("Is uw kind in de afgelopen 3 maanden afgevallen, zonder aanwijsbare reden (ziekte)?", [0, 0, 3]),
    ("Toont uw kind interesse in eten?", [2, 1, 0]),
    ("Weigert uw kind vanaf de geboorte bepaalde producten te eten?", [0, 1, 3]),
    ("Heeft uw kind voorkeur voor bepaalde smaken of structuren (krokant, glad, vloeibaar, zacht voedsel etc.)?", [0, 1, 3]),
    ("Heeft uw kind bij de introductie vaste voeding alles leren eten?", [3, 1, 0]),
    ("Heeft uw kind problemen met het kauwen en/of slikken van het eten?", [0, 1, 3]),
    ("Geniet uw kind van het eten?", [2, 1, 0]),
    ("Klaagt uw kind over misselijkheid of buikpijn?", [0, 1, 2]),
    ("Vraagt uw kind zelf om eten?", [2, 0, 0]),
    ("Lust uw kind de ene dag iets wel en de andere dag niet?", [2, 1, 0]),
    ("Weigert uw kind zowel overdag als tijdens het avondeten voedsel?", [0, 1, 2]),
]

antwoord_opties = ["Nee", "Soms", "Ja"]

# Variabelen voor antwoorden
score = 0
valid = True

with st.form("vragenlijst_form"):
    antwoorden = []
    for idx, (vraag, punten) in enumerate(vragen):
        antwoord = st.radio(f"{idx+1}. {vraag}", antwoord_opties, key=idx)
        antwoord_index = antwoord_opties.index(antwoord)
        punt = punten[antwoord_index]
        if punt is None:
            valid = False
        antwoorden.append(punt)
    submitted = st.form_submit_button("Verstuur")

# Berekening en advies
if submitted:
    if not valid:
        st.error("Deze combinatie van antwoorden is ongeldig.")
    else:
        score = sum(antwoorden)

        # Advies tonen met neutrale (zwarte) tekst
        if score < 10:
            st.markdown(
                "<div style='background-color:#d9fdd3;padding:15px;border-radius:10px;'><b>✅ Advies:</b> Er zijn geen directe zorgen over het eetgedrag van uw kind. <br> <a href='#' style='color:darkgreen;'>Volg deze link voor tips.</a></div>",
                unsafe_allow_html=True
            )
        elif 10 <= score < 15:
            st.markdown(
                "<div style='background-color:#fff4cc;padding:15px;border-radius:10px;'><b>⚠️ Advies:</b> Er zijn enkele aandachtspunten. Houd het gedrag in de gaten en bekijk <a href='#' style='color:darkgreen;'>dit document voor tips.</a></div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div style='background-color:#ffe6e6;padding:15px;border-radius:10px;'><b>❗ Advies:</b> De score wijst op mogelijke eetproblemen. <br>Neem <a href='#' style='color:darkred;'>contact op met een diëtist.</a></div>",
                unsafe_allow_html=True
            )
