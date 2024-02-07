import streamlit as st
from htmlTemplates import css, button_template, card_template
from streamlit_card import card

st.set_page_config(page_title="AI Generation Tools", layout="centered")

# st.title("AI Generation Tools")

col1, col2, col3 = st.columns(3)

with col1:
    st.button("📷Image", use_container_width=True, type="primary")
with col2:
    st.button("📊Flowchart", use_container_width=True, type="primary")
with col3:
    st.button("🖼️Presentation", use_container_width=True, type="primary")

col4, col5, col6 = st.columns([1, 1, 1], gap="large")

# with col4:
#     for i in range(1, 3):
#         cols = card(
#             key=str(i),
#             title="Hello World!",
#             text="Some description",
#             image="http://placekitten.com/200/300",
#             url="https://github.com/gamcoh/st-card"
#         )
#
# with col5:
#     for i in range(1, 3):
#         cols = card(
#             key=str(i + 10),
#             title="Streamlit Card",
#             text="This is a test card",
#             image="https://placekitten.com/500/500",
#             styles={
#                 "card": {
#                     "width": "300px",
#                     "height": "250px",
#                     "border-radius": "20px",
#                     "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
#                 },
#                 "title": {
#                     "color": "red",
#                 },
#             },
#         )
#
# with col6:
#     for i in range(1, 3):
#         cols = card(
#             key=str(i+20),
#             title="Hello World!",
#             text="Some description",
#             image="http://placekitten.com/200/300",
#             url="https://github.com/gamcoh/st-card"
#         )

st.container(height=650, border=False)
web_search_toggle, chat_input = st.columns([0.2, 0.8])
with web_search_toggle:
    st.toggle(label="Web Search")
with chat_input:
    user_question = st.chat_input("Message BofA-GPT...")
