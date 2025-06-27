import streamlit as st

# Pagina-configuratie
st.set_page_config(page_title="Eetgedrag Vragenlijst", layout="centered")

# Intro en uitleg
st.markdown("### 🌟 De PeuterEetCompas: Vragenlijst met passend advies")
st.markdown("<span style='color:darkgreen;font-size:18px;'>Deze vragenlijst is voor ouders van kinderen tussen 1 en 6 jaar oud. Beantwoord de vragen door 'Nee', 'Soms' of 'Ja' aan te kruisen. Aan het einde krijgt u op basis van uw antwoorden een passend advies met betrekking tot het eetgedrag van uw kind.</span>", unsafe_allow_html=True)
st.markdown("<span style='color:red;font-size:18px;'>Let op: voor een betrouwbaar advies moet u elke vraag zorgvuldig beantwoorden.</span>", unsafe_allow_html=True)

# CSS-styling
st.markdown("""
    <style>
    .stApp { background-color: #e6ffe6; color: black; }
    label { color: black !important; font-weight: bold; }
    div[data-testid="stRadio"] { background-color: #006400; padding: 12px; border-radius: 10px; margin-bottom: 16px; }
    div[data-testid="stRadio"] *, div[data-testid="stRadio"] label { color: white !important; }
    button[kind="primary"] {
        background-color: #006400; color: white; border-radius: 8px; padding: 10px 20px; font-size: 16px;
    }
    button[kind="primary"]:hover {
        background-color: #228B22; color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Titel
st.title("Vragenlijst over het eetgedrag van uw kind")

# Vragen: (vraagtekst, kleur, punten [Nee, Soms, Ja])
vragen = [
    ("Kokhalst uw kind tijdens de maaltijd?", "blauw", [0, 1, 2]),
    ("Is uw kind in de afgelopen 3 maanden afgevallen, zonder aanwijsbare reden (ziekte)?", "blauw", [0, 1, 2]),
    ("Heeft u kind bij de introductie vaste voeding alles leren eten?", "blauw", [2, 1, 0]),
    ("Heeft uw kind problemen met het kauwen en of slikken van het eten?", "blauw", [0, 1, 2]),
    ("Eet uw kind minder dan aanbevolen hoeveelheid voor zijn of haar leeftijd?", "blauw", [0, 1, 2]),
    ("Klaagt uw kind over misselijkheid of buikpijn?", "blauw", [0, 1, 2]),
    ("Heeft uw kind een sterke voorkeur voor bepaalde producten?", "roze", [0, 1, 2]),
    ("Weigert uw kind nieuwe producten te proberen?", "roze", [0, 1, 2]),
    ("Eet uw kind elke dag dezelfde producten?", "roze", [0, 1, 2]),
    ("Heeft uw kind sondevoeding gehad?", "oranje", [0, 1, 2]),
    ("Toont uw kind spanning, zoals huilen of wegdraaien, tijdens eetmomenten?", "groen", [0, 1, 2]),
    ("Heeft uw kind zich ooit ernstig verslikt in eten?", "oranje", [0, 0, 2]),
    ("Is uw kind een keer ziek geworden van eten met ernstige buikpijn en/of overgeven?", "oranje", [0, 1, 2]),
    ("Toont uw kind interesse in eten?", "groen", [2, 1, 0]),
    ("Weigert uw kind vanaf de geboorte bepaalde producten te eten?", "roze", [0, 1, 2]),
    ("Heeft u kind voorkeur voor bepaalde smaken of structuren (krokant, glad vloeibaar, zacht voedsel etc.)?", "roze", [0, 1, 2]),
    ("Geniet uw kind van het eten?", "groen", [2, 1, 0]),
    ("Vraagt uw kind zelf om eten?", "groen", [2, 0, 0]),
    ("Lust uw kind de ene dag iets wel en de andere dag niet?", "groen", [2, 1, 0]),
    ("Weigert uw kind zowel overdag als tijdens het avondeten voedsel?", "roze", [0, 1, 2])
]

antwoord_opties = ["Nee", "Soms", "Ja"]

# Puntentelling per kleurcategorie
kleuren_scores = {"blauw": 0, "roze": 0, "groen": 0, "oranje": 0}

with st.form("vragenlijst_form"):
    for idx, (vraag, kleur, punten) in enumerate(vragen):
        antwoord = st.radio(f"{idx+1}. {vraag}", antwoord_opties, key=idx)
        antwoord_index = antwoord_opties.index(antwoord)
        score = punten[antwoord_index]
        kleuren_scores[kleur] += score

    submitted = st.form_submit_button("Verstuur")

if submitted:
    def bepaal_adviesniveau(kleur, score):
        if kleur in ["blauw", "roze"]:
            if score > 8:
                return 3
            elif 5 <= score <= 8:
                return 2
            else:
                return 1
        elif kleur == "groen":
            if score > 4:
                return 3
            elif 2 <= score <= 4:
                return 2
            else:
                return 1
        elif kleur == "oranje":
            if score > 2:
                return 3
            elif score == 1:
                return 2
            else:
                return 1

    # Adviesniveaus verzamelen
    adviesniveaus = [bepaal_adviesniveau(kleur, score) for kleur, score in kleuren_scores.items()]
    hoogste_adviesniveau = max(adviesniveaus)

    # Adviesblokken
    adviezen_html = {
        1: """
        <div style='background-color:#e6ffe6;padding:15px;border-radius:10px;'>
        <b>✅ Advies:</b> Er zijn geen aanwijzingen tot problematisch kritisch eetgedrag. 
        Het eetgedrag van uw peuter kan vervelend zijn, maar hoort waarschijnlijk bij de leeftijd. 
        Klik <a href='https://drive.google.com/file/d/1mXb6XCj252KMXJ0QyRMJPp803jLvowFk/view?usp=sharing' 
        style='color:darkgreen;' target='_blank'>hier</a> voor de brochure <i>Stapjes naar meer hapjes</i> 
        met eenvoudige, praktische adviezen om het eetgedrag van hun kind te ondersteunen.
        </div>
        """,
        2: """
        <div style='background-color:#fff4cc;padding:15px;border-radius:10px;'>
        <b>⚠️ Advies:</b> Ouders worden aangeraden om het eetgedrag van hun kind actief te observeren 
        en de tips uit <i>Stapjes naar meer hapjes</i> toe te passen. 
        Klik <a href='https://drive.google.com/file/d/1mXb6XCj252KMXJ0QyRMJPp803jLvowFk/view?usp=sharing' 
        style='color:darkgreen;' target='_blank'>hier</a> voor de brochure. 
        Als het gedrag na enkele weken niet verbetert of verslechtert, kan het nuttig zijn om alsnog een volgende stap te overwegen, 
        zoals een afspraak bij een huisarts of consultatiebureau.
        </div>
        """,
        3: """
        <div style='background-color:#ffe6e6;padding:15px;border-radius:10px;'>
        <b>❗ Advies:</b> Er wordt geadviseerd om contact op te nemen met een diëtist. 
        De diëtist kan helpen om de achterliggende oorzaken van het eetgedrag in kaart te brengen 
        (bijvoorbeeld medische of psychologische factoren) en een gerichte aanpak bieden om het eetgedrag van het kind te verbeteren. 
        Klik <a href='https://www.nvdietist.nl/ik-zoek-een-dietist/' style='color:darkred;' target='_blank'>hier</a> 
        om een diëtist te vinden, of 
        <a href='https://deniedietisten.nl/contactgegevens/' style='color:darkred;' target='_blank'>hier</a> 
        om contact op te nemen met De Nie diëtisten.
        </div>
        """
    }

    # Toon slechts het hoogste noodzakelijke advies
    st.markdown(adviezen_html[hoogste_adviesniveau], unsafe_allow_html=True)
