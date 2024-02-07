import streamlit as st
from htmlTemplates import css, button_template, card_template
from streamlit_card import card
st.set_page_config(layout="wide")

st.title("AI Generation Tools")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.button("🐍Python")
with col2:
    st.button("📀SQL")
with col3:
    st.button("📊Flowchart")
with col4:
    st.button("✏️Summarize")
with col5:
    st.button("🖼️Presentation")
with col6:
    st.button("📧Email")


# Cards grid
for i in range(1, 5):
    cols = st.columns(2)
    cols[0] = card(
        key=str(i),
        title="Hello World!",
        text="Some description",
        image="http://placekitten.com/200/300",
        url="https://github.com/gamcoh/st-card"
    )
    cols[1] = card(
        key=str(i+10),
        title="Streamlit Card",
        text="This is a test card",
        image="https://placekitten.com/500/500",
        styles={
            "card": {
                "width": "500px",
                "height": "500px",
                "border-radius": "60px",
                "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            },
            "title": {
                "color": "red",
            },
        },
)
