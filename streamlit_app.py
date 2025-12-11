import streamlit as st
import pandas as pd

st.title('Penguin Identifier')

st.info('This is a machine learning app')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

df
