import streamlit as st

# Pagina-configuratie
st.set_page_config(page_title="Eetgedrag Vragenlijst", layout="centered")

st.title("Vragenlijst over het eetgedrag van uw kind")

# Vragen en puntensysteem
vragen = [
    ("Heeft uw kind een sterke voorkeur voor bepaalde producten?", [0, 1, 2]),
    ("Weigert uw kind nieuwe producten te proberen?", [0, 1, 2]),
    ("Eet uw kind elke dag dezelfde producten?", [0, 1, 2]),
    ("Eet uw kind minder dan aanbevolen hoeveelheid voor zijn of haar leeftijd?", [0, 1, 2]),
    ("Lijkt uw kind angstig of gestrest rond eetmomenten?", [0, 1, 2]),
    ("Kokhalst uw kind tijdens de maaltijd?", [0, 1, 2]),
    ("Is uw kind in de afgelopen 3 maanden afgevallen, zonder aanwijsbare reden (ziekte)?", [0, None, 3]),
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

        st.subheader("Uw totaalscore is:")
        st.success(f"{score} punten")

        if score < 15:
            st.info("✅ Advies: Er zijn geen directe zorgen over het eetgedrag van uw kind. Volg deze link voor tips.")
        elif 15 <= score < 30:
            st.warning("⚠️ Advies: Er zijn enkele aandachtspunten. Houd het gedrag in de gaten en bekijken dit document voor tips.")
        else:
            st.error("❗ Advies: De score wijst op mogelijke eetproblemen. Neem contact op met een kinderarts of diëtist.")



