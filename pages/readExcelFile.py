import streamlit as st
import pandas
import os

def drawExcelFilePage():
    current_file = os.path.abspath(os.path.dirname(__file__))
    csv_file = os.path.join(current_file, '..', 'resources', '초등-영어-단어-모음-800개.csv')
    csv_read= pandas.read_csv(csv_file)
    df = pandas.DataFrame(csv_read)
    st.dataframe(df)

