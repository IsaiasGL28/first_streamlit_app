import streamlit as st
import pandas as pd

st.title('Fruits dataframe')
fruits_df = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruits_df = fruits_df.set_index('Fruit')
fruits_list = list(fruits_df.index)
fruits_selected = st.multiselect('Pick some fruits: ', fruits_list, fruits_list[:2])
df_to_show = fruits_df.loc[fruits_selected]
st.dataframe(df_to_show)
