import streamlit as st
from chat_engine import get_response

st.set_page_config(page_title="SIUC Assistant", layout="wide")
st.title("🧠 SIUC Simulation Assistant (CPTA)")
st.caption("Powered by StratDesign Solutions • Tailored for Southern Illinois University Carbondale")

with st.chat_message("assistant"):
    st.markdown("How can I help you today with simulation coordination, training, or job requirements?")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input("Ask about training, scheduling, qualifications, or support...")

if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        response = get_response(query)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Optional section placeholder
st.header("📊 Browse Simulation Data")
st.info("Sample data will be available soon.")