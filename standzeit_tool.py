import streamlit as st
import math

# Seiteneinstellungen
st.set_page_config(page_title="Standzeit-Berechnung", page_icon="🚗", layout="centered")
st.title("🚗 Standzeit-Berechnungstool")
st.write("""
Dieses Tool berechnet die technisch notwendige Reparaturdauer (Standtage) 
auf Basis der Spengler-, Lackierer- und Mechanikerstunden. 
Zusätzlich können Trocknungs- oder organisatorische Verzögerungstage angegeben werden.
""")

# Eingaben
st.subheader("Eingaben")
spengler = st.number_input("Spenglerstunden", min_value=0.0, step=0.5)
lackierer = st.number_input("Lackierstunden", min_value=0.0, step=0.5)
mechaniker = st.number_input("Mechanikerstunden", min_value=0.0, step=0.5)
zusatztage = st.number_input("Zusatz-/Trocknungstage", min_value=0, step=1)

# Berechnung
gesamtstunden = spengler + lackierer + mechaniker
arbeitstage_gerundet = math.ceil(gesamtstunden / 8) if gesamtstunden > 0 else 0
gesamtstandtage = arbeitstage_gerundet + zusatztage

# Ausgabe
if st.button("Berechnen"):
    st.subheader("📊 Ergebnis")
    st.write(f"**Gesamtstunden:** {gesamtstunden:.1f} h")
    st.write(f"**Arbeitstage (gerundet):** {arbeitstage_gerundet} Tage")
    st.write(f"**Zusatz-/Trocknungstage:** {zusatztage} Tage")
    st.write(f"**Technische Standzeit gesamt:** {gesamtstandtage} Tage")

    # Gutachten-Textbaustein
    st.subheader("📝 Textbaustein fürs Gutachten")
    textbaustein = (
        f"Die technische Reparaturdauer beträgt {gesamtstandtage} Arbeitstage "
        f"aufgrund von {gesamtstunden:.1f} Gesamtstunden "
        f"und {zusatztage} zusätzlichen Tagen für Trocknung oder organisatorische Abläufe."
    )
    st.code(textbaustein, language="text")
