import streamlit as st

# Pagina-configuratie
st.set_page_config(page_title="Eetgedrag Vragenlijst", layout="centered")

# Intro en uitleg
st.markdown("### 🌟 De PeuterEetCompas: Vragenlijst met passend advies")
st.markdown("<span style='color:darkgreen;font-size:18px;'>Deze vragenlijst is voor ouders van kinderen tussen 1 en 6 jaar.Beantwoord de vragen door 'Nee', 'Soms' of 'Ja' aan te kruisen. Aan het einde krijgt u op basis van uw antwoorden een passend advies met betrekking tot het eetgedrag van uw kind.</span>", unsafe_allow_html=True)
st.markdown("<span style='color:red;font-size:18px;'>Let op: voor een betrouwbaar advies moet u elke vraag zorgvuldig beantwoorden.</span>", unsafe_allow_html=True)

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
    ("Eet uw kind minder dan aanbevolen hoeveelheid voor zijn of haar leeftijd? De aanbevolen hoeveelheid kunt u vinden op de website van het voedingscentrum", [0, 2, 8] )
    ("Kokhalst uw kind tijdens de maaltijd?", [0, 2, 8]),
    ("Is uw kind in de afgelopen 3 maanden afgevallen, zonder aanwijsbare reden (ziekte)?", [0, 2, 8]),
    ("Heeft uw kind bij de introductie vaste voeding alles leren eten?", [8, 2, 0]),
    ("Heeft uw kind problemen met het kauwen en of slikken van het eten?", [0, 2, 8]),
    ("Klaagt uw kind over misselijkheid of buikpijn?", [0, 2, 8]),
    ("Heeft uw kind een sterke voorkeur voor bepaalde producten?", [0, 2, 8]),
    ("Weigert uw kind nieuwe producten te proberen?", [0, 2, 8]),
    ("Eet uw kind elke dag dezelfde producten?", [0, 2, 8]),
    ("Heeft uw kind sondevoeding gehad?", [0, 1, 2]),
    ("Toont uw kind spanning, zoals huilen of wegdraaien, tijdens eetmomenten?", [0, 2, 4]),
    ("Heeft uw kind zich ooit ernstig verslikt in eten?", [0, 0, 2]),
    ("Is uw kind een keer ziek geworden van eten met ernstige buikpijn en/of overgeven?", [0, 1, 2]),
    ("Toont uw kind interesse in eten?", [4, 1, 0]),
    ("Weigert uw kind vanaf de geboorte bepaalde producten te eten?", [0, 2, 8]),
    ("Heeft uw kind voorkeur voor bepaalde smaken of structuren (krokant, glad, vloeibaar, zacht voedsel etc.)?", [0, 2, 8]),
    ("Geniet uw kind van het eten?", [4, 2, 0]),
    ("Vraagt uw kind zelf om eten?", [4, 0, 0]),
    ("Lust uw kind de ene dag iets wel en de andere dag niet?", [4, 2, 0]),
    ("Weigert uw kind zowel overdag als tijdens het avondeten voedsel?", [0, 2, 8])
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
                "<b>✅ Advies:</b> Bij een score onder de 8 zijn er geen aanwijzingen tot problematisch kritisch eetgedrag. "
                "Het eetgedrag van uw peuter kan vervelend zijn, maar hoort waarschijnlijk bij de leeftijd. "
                "Klik <a href='https://github.com/RomyBrink/Eetgedrag/blob/main/AvoidantRestrictive_Food_Intake_Disorder_A_Longitu.pdf' "
                "style='color:darkgreen;' target='_blank'>hier</a> voor de brochure <i>Stapjes naar meer hapjes</i> met eenvoudige, praktische adviezen om het eetgedrag van hun kind te ondersteunen."
                "</div>",
                unsafe_allow_html=True
            )
        if 8 <= score <= 12:
            st.markdown(
                "<div style='background-color:#fff4cc;padding:15px;border-radius:10px;'>"
                "<b>⚠️ Advies:</b> Een score tussen 8 en 12 wijst op eetgedrag dat aandacht vraagt, maar nog niet direct zorgwekkend is. "
                "Ouders worden aangeraden om het eetgedrag van hun kind actief te observeren en de tips uit <i>Stapjes naar meer hapjes</i> toe te passen. "
                "Klik <a href='https://github.com/RomyBrink/Eetgedrag/blob/main/AvoidantRestrictive_Food_Intake_Disorder_A_Longitu.pdf' "
                "style='color:darkgreen;' target='_blank'>hier</a> voor de brochure. Als het gedrag na enkele weken niet verbetert of verslechtert, "
                "kan het nuttig zijn om alsnog een volgende stap te overwegen, zoals een afspraak bij een huisarts of consultatiebureau."
                "</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div style='background-color:#ffe6e6;padding:15px;border-radius:10px;'>"
                "<b>❗ Advies:</b> Bij een score boven de 12 wordt er geadviseerd om contact op te nemen met een diëtist. "
                "De diëtist kan helpen om de achterliggende oorzaken van het eetgedrag in kaart te brengen (bijvoorbeeld medische of psychologische factoren) "
                "en een gerichte aanpak bieden om het eetgedrag van het kind te verbeteren. "
                "Klik <a href='https://www.nvdietist.nl/ik-zoek-een-dietist/' style='color:darkred;' target='_blank'>hier</a> om een diëtist te vinden, of "
                "<a href='https://deniedietisten.nl/contactgegevens/' style='color:darkred;' target='_blank'>hier</a> om contact op te nemen met De Nie diëtisten."
                "</div>",
                unsafe_allow_html=True
            )

