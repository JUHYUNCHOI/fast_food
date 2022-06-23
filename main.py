import streamlit as st
from pages import fastfood, readExcelFile,crimeLocation

choice = st.sidebar.selectbox('Select: ', ['선택하세요.', 'FastFood', 'ExcelFile', '범죄발생지결과'])

if choice == 'FastFood':
    fastfood.drawFastFoodPage()
elif choice == 'ExcelFile':
    readExcelFile.drawExcelFilePage()
elif choice == '범죄발생지결과':
    crimeLocation.drawCrimeLocationPage()


