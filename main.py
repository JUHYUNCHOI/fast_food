import streamlit as st
from pages import fastfood, readExcelFile

choice = st.sidebar.selectbox('Select: ', ['선택하세요.', 'FastFood', 'ExcelFile'])

if choice == 'FastFood':
    fastfood.drawFastFoodPage()
elif choice == 'ExcelFile':
    readExcelFile.drawExcelFilePage()


