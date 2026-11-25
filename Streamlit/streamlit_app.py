import streamlit as st
import requests

st.set_page_config("Marriage Stability Predictor")
st.markdown("""
<div style='text-align:center;'>
    <h1 style='margin-bottom:0px;'>Marriage Stability Predictor</h1>
</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("Questions")
st.write("")
st.write("")

st.markdown("""
<div style='text-align:center; color:#F44B4B;'>
    <p style='margin-bottom:5px;'>5-point frequency Likert scale:</p>
    <p style='margin-top:0px;'>
        0 = 'Never' &nbsp;&nbsp;&nbsp;
        1 = 'Rarely' &nbsp;&nbsp;&nbsp;
        2 = 'Sometimes' &nbsp;&nbsp;&nbsp;
        3 = 'Often' &nbsp;&nbsp;&nbsp;
        4 = 'Always'
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

st.markdown("""Answer the questions below to assess whether your relationship is stable""")

st.write("")
st.write("")
st.write("")
st.write("")

col1, col2 = st.columns([1,1])

with col1:
    st.markdown("<div style='font-size:14px; height:40px;'>When we need it, we can take our discussions with my spouse from the beginning and correct it</div>", unsafe_allow_html=True)
    correct = st.slider("", 0, 4, 2, key="correct_slider")
    st.divider()
    st.markdown("<div style='font-size:14px; height:40px;'>We're just starting a discussion before I know what's going on</div>", unsafe_allow_html=True)
    idk = st.slider("", 0, 4, 2, key="idk_slider")
    st.divider()
    st.markdown("<div style='font-size:14px; height:40px;'>My spouse and I have similar values in trust</div>", unsafe_allow_html=True)
    trust = st.slider("", 0, 4, 2, key="trust_slider")

with col2:
    st.markdown("<div style='font-size:14px; height:40px;'>Sometimes I think it's good for me to leave home for a while</div>", unsafe_allow_html=True)
    good = st.slider("", 0, 4, 2, key="good_slider")
    st.divider()
    st.markdown("<div style='font-size:14px; height:40px;'>I know my spouse's basic anxieties</div>", unsafe_allow_html=True)
    anxieties = st.slider("", 0, 4, 2, key="anxieties_slider")
    st.divider()
    st.markdown("<div style='font-size:14px; height:40px;'>I have nothing to do with what I've been accused of</div>", unsafe_allow_html=True)
    accusations = st.slider("", 0, 4, 2, key="accusations_slider")

payload = {
    "begin_correct": correct,
    "idk_what_s_going_on": idk,
    "trust": trust,
    "good_to_leave_home": good,
    "anxieties": anxieties,
    "accusations": accusations,
}

st.divider()

if st.button("Predict marriage stability"):
    response = requests.post("https://marriage-prediction-api.onrender.com/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        prediction = result.get("prediction")
        message = result.get("message")

        if prediction == 1:
            st.success(message)
        else:
            st.warning(message)

    else:
        st.error("Error while calling the API")
