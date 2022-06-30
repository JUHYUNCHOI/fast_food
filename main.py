# import streamlit as st
# from pages import fastfood, readExcelFile,crimeLocation, upAndDown
# st.set_page_config(layout="wide")
# choice = st.sidebar.selectbox('Select: ', ['선택하세요.', 'FastFood', 'ExcelFile', '범죄발생지결과', '업앤다운게임'])
#
# if choice == 'FastFood':
#     fastfood.drawFastFoodPage()
# elif choice == 'ExcelFile':
#     readExcelFile.drawExcelFilePage()
# elif choice == '범죄발생지결과':
#     crimeLocation.drawCrimeLocationPage()
#
# elif choice == '업앤다운게임':
#     upAndDown.drawUpAndDownGamePage()
#

from pages import upAndDown
import streamlit as st


choice = st.sidebar.selectbox('선택: ', ['업앤다운게임', 'aaaa', 'bbbb'])

if choice == '업앤다운게임':
    upAndDown.drawUpAndDownGamePage()




















