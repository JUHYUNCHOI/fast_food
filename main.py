import streamlit as st
from pages import fastfood

choice = st.sidebar.selectbox('Select: ', ['선택하세요.', 'FastFood'])

if choice == 'FastFood':
    fastfood.drawFastFoodPage()


