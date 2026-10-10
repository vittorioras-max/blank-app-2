import streamlit as st

# 1. Titolo della pagina
st.set_page_config(page_title="Assistente di Famiglia", page_icon="🤖")
st.title("🤖 Assistente di Famiglia")

# 2. Controllo della Password (per far entrare solo te e tua moglie)
# (Puoi cambiare "1234" con la password che preferisci)
password_inserita = st.text_input("Inserisci la password di accesso:", type="password")

if password_inserita != "1234":
    if password_inserita != "":
        st.error("Password errata.")
    st.stop() # Blocca il caricamento finché la password non è corretta

st.success("Accesso consentito!")

# 3. Gestione della cronologia della chat
# Serve a ricordare i messaggi scritti durante la conversazione
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra i messaggi passati
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Casella di input in basso per scrivere i messaggi
if prompt := st.chat_input("Scrivi qui la tua richiesta..."):
    
    # Salva e mostra il messaggio dell'utente
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 5. La risposta del bot (per ora simulata)
    # Qui un domani collegheremo i tuoi script Python o l'IA con i paletti rigidi!
    with st.chat_message("assistant"):
        if "meteo" in prompt.lower() or "vento" in prompt.lower():
            risposta = "Ho controllato: al momento la situazione meteo è sotto controllo."
        elif "traffico" in prompt.lower():
            risposta = "Il tragitto casa-lavoro è scorrevole."
        else:
            risposta = f"Ho ricevuto la tua richiesta: '{prompt}'. (Al momento rispondo solo a meteo e traffico per sicurezza!)"
            
        st.markdown(risposta)
    
    # Salva la risposta nella cronologia
    st.session_state.messages.append({"role": "assistant", "content": risposta})
    
