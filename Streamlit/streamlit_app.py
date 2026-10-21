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
    st.markdown("<div style='font-size:14px; height:40px;'>I enjoy traveling with my wife</div>", unsafe_allow_html=True)
    travel = st.slider("", 0, 4, 2, key="travel_slider")
    st.divider()
    st.markdown("<div style='font-size:14px; height:40px;'>I think my spouse and I are in harmony</div>", unsafe_allow_html=True)
    harmony = st.slider("", 0, 4, 2, key="harmony_slider")
    st.divider()
    st.markdown("<div style='font-size:14px; height:40px;'>Our dreams are similar and harmonious</div>", unsafe_allow_html=True)
    dreams = st.slider("", 0, 4, 2, key="dreams_slider")
    st.divider()
    st.markdown("<div style='font-size:14px; height:40px;'>We share the same views about being happy in our life</div>", unsafe_allow_html=True)
    happy = st.slider("", 0, 4, 2, key="happy_slider")
    st.divider()
    st.markdown("<div style='font-size:14px; height:40px;'>My spouse and I have similar ideas about how marriage should be</div>", unsafe_allow_html=True)
    marriage = st.slider("", 0, 4, 2, key="marriage_slider")

with col2:
    st.markdown("<div style='font-size:14px; height:40px;'>I know my spouse's basic anxieties</div>", unsafe_allow_html=True)
    anxieties = st.slider("", 0, 4, 2, key="anxieties_slider")
    st.divider()
    st.markdown("<div style='font-size:14px; height:40px;'>I feel aggressive when I argue with my spouse</div>", unsafe_allow_html=True)
    aggro = st.slider("", 0, 4, 2, key="aggressive_slider")
    st.divider()
    st.markdown("<div style='font-size:14px; height:40px;'>I hate my spouse's way of opening a subject</div>", unsafe_allow_html=True)
    hate = st.slider("", 0, 4, 2, key="hate_slider")
    st.divider()
    st.markdown("<div style='font-size:14px; height:40px;'>We're just starting a discussion before I know what's going on</div>", unsafe_allow_html=True)
    idk = st.slider("", 0, 4, 2, key="idk_slider")
    st.divider()
    st.markdown("<div style='font-size:14px; height:40px;'>Sometimes I think it's good for me to leave home for a while</div>", unsafe_allow_html=True)
    good = st.slider("", 0, 4, 2, key="good_slider")

payload = {
    "enjoy_travel": travel,
    "harmony": harmony,
    "dreams": dreams,
    "happy": happy,
    "marriage": marriage,
    "anxieties": anxieties,
    "Aggro_argue": aggro,
    "hate_subjects": hate,
    "idk_what_s_going_on": idk,
    "good_to_leave_home": good
}

st.divider()

if st.button("Predict marriage stability"):
    response = requests.post("https://marriage-prediction-api.onrender.com/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        prediction = result.get("prediction")
        message = result.get("message")

        if prediction == 0:
            st.success("Your marriage has a good chance of lasting!")
        else:
            st.warning("Your relationship has some vulnerabilities")

    else:
        st.error("Error while calling the API")
