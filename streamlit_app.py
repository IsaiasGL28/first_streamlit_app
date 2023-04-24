import streamlit as st
import pandas as pd

st.title('Fruits dataframe')
fruits_df = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruits_df.set_index('Fruit')
st.multiselect('Pick some fruits: ', list(fruits_df.index))
st.dataframe(fruits_df)
