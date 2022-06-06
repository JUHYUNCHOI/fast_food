import requests
import streamlit as st

head = st.container()
body = st.container()
foot = st.container()


search_input = head.text_input('검색: ', '검색어를 입력하세요.')
search_button = head.button('검색')
