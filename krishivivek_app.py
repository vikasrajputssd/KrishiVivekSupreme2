import streamlit as st
import pandas as pd
from datetime import date

st.title("🌿 KrishiVivek Supreme - किसान सब्जी एंट्री")

def save_data(data):
    df = pd.DataFrame([data])
    df.to_csv("krishi_data.csv", mode='a', header=False, index=False)

with st.form(key='entry_form'):
    farmer = st.text_input("👨‍🌾 किसान का नाम")
    sabzi = st.text_input("🥦 सब्जी का नाम")
    todai = st.date_input("📅 तोड़ने की तारीख", date.today())
    quantity = st.number_input("📊 मात्रा (किलो में)", min_value=0)
    transport = st.selectbox("🚚 ट्रांसपोर्ट का तरीका", ["ट्रैक्टर", "पिकअप", "टेम्पो", "अन्य"])
    mandi = st.date_input("🏬 मंडी पहुँचने की तारीख", date.today())
    rate = st.number_input("💰 मंडी में भाव (₹ प्रति किलो)", min_value=0)
    location = st.text_input("📍 मंडी का नाम/स्थान")
    
    submit_button = st.form_submit_button(label='✅ डेटा सहेजें')

if submit_button:
    data = {
        "किसान": farmer,
        "सब्जी": sabzi,
        "तोड़ने की तारीख": str(todai),
        "मात्रा": quantity,
        "ट्रांसपोर्ट": transport,
        "मंडी तारीख": str(mandi),
        "भाव": rate,
        "मंडी स्थान": location
    }
    save_data(data)
    st.success(f"✅ डेटा सफलतापूर्वक सहेजा गया!\n\nकिसान: {farmer}\nसब्जी: {sabzi}\nमात्रा: {quantity} किलो\nमंडी: {location}")

if st.button("डेटा देखें"):
    try:
        df = pd.read_csv("krishi_data.csv", names=["किसान","सब्जी","तोड़ने की तारीख","मात्रा","ट्रांसपोर्ट","मंडी तारीख","भाव","मंडी स्थान"])
        st.dataframe(df)
    except FileNotFoundError:
        st.warning("कोई डेटा अभी तक सेव नहीं हुआ है।")
